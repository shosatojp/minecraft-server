import json
import re
import bs4
import sys
from pprint import pprint
from get_html import get_html
import packaging.version
import termcolor


def get_download_link(version: str) -> str:
    html = get_html(f'https://mcversions.net/download/{version}')
    doc = bs4.BeautifulSoup(html, 'html.parser')
    button = doc.select_one('.downloads div:nth-child(1) a')
    if button:
        return button.get('href')


def get_versions():
    html = get_html('https://mcversions.net/')
    doc = bs4.BeautifulSoup(html, 'html.parser')

    # find stable releases
    stable_releases_header = doc.select_one('h5:first-child')
    assert(stable_releases_header.text == 'Stable Releases')
    stable_releases = stable_releases_header.parent

    # get versions
    versions = [e.get('id') for e
                in stable_releases.select('.item') if e.get('id')]

    for version in versions:
        termcolor.cprint(version, 'grey', file=sys.stderr)
        server = get_download_link(version)
        if server:
            if packaging.version.Version(version) >= packaging.version.Version('1.17'):
                termcolor.cprint(f'{version} {server}', 'green')
                yield {
                    'version': f'{version}',
                    'type': 'vanilla',
                    'server': server,
                    'java': 16,
                }
            else:
                termcolor.cprint(f'{version} {server}', 'green')
                yield {
                    'version': f'{version}',
                    'type': 'vanilla',
                    'server': server,
                    'java': 8,
                }
        else:
            termcolor.cprint(f'server file not found for version:{version}', 'red', file=sys.stderr)


def get_forge_version(version: str):
    termcolor.cprint(version, 'grey', file=sys.stderr)
    html = get_html(f'http://files.minecraftforge.net/net/minecraftforge/forge/index_{version}.html')
    doc = bs4.BeautifulSoup(html, 'html.parser')

    installer = doc.select_one('.downloads > .download:last-child > .links > .link > a[title=Installer]')
    installer_link = installer and re.match('.*url=(.*)$', installer.get('href'))[1]

    universal = doc.select_one('.downloads > .download:last-child > .links > .link > a[title=Universal]')
    universal_link = universal and re.match('.*url=(.*)$', universal.get('href'))[1]

    return (installer_link,  universal_link)


def get_forge_versions():
    html = get_html('http://files.minecraftforge.net/')
    doc = bs4.BeautifulSoup(html, 'html.parser')
    versions = [e.text.strip() for e
                in doc.select('.li-version-list li')]
    for version in versions:
        installer, universal = get_forge_version(version)

        if packaging.version.Version(version) >= packaging.version.Version('1.17'):
            termcolor.cprint(f'forge-{version} run {installer} {universal}', 'green')
            yield {
                'version': f'forge-{version}',
                'type': 'forge-run',
                'installer': installer,
                'java': 16,
            }
        elif installer and universal:
            termcolor.cprint(f'forge-{version} universal {installer} {universal}', 'green')
            yield {
                'version': f'forge-{version}',
                'type': 'forge-universal',
                'universal': universal,
                'installer': installer,
                'java': 8,
            }
        elif installer:
            termcolor.cprint(f'forge-{version} installer {installer}', 'green')
            yield {
                'version': f'forge-{version}',
                'type': 'forge-installer',
                'installer': installer,
                'java': 8,
            }
        else:
            termcolor.cprint(f'nofile, skip. {version}', 'yellow', file=sys.stderr)


def get_fabric_versions():
    src = get_html('https://meta.fabricmc.net/v2/versions/installer')
    jsonobj = json.loads(src)

    installer = jsonobj[0]['url']

    yield {
        'version': f'fabric',
        'type': 'fabric',
        'installer': installer,
        'java': 8,
    }


versions_file = 'versions.json'
versions = [*get_versions(), *get_forge_versions(), *get_fabric_versions()]
with open(versions_file, 'wt', encoding='utf-8') as f:
    json.dump(versions, f, ensure_ascii=False, indent=4)
print(f'dumped to {versions_file}')
