import re
import requests
import bs4
import sys


def get_download_link(version: str) -> str:
    html = requests.get(f'https://mcversions.net/download/{version}').text
    doc = bs4.BeautifulSoup(html, 'html.parser')
    button = doc.select_one('.downloads div:nth-child(1) a')
    if button:
        return button.get('href')


def get_versions():
    html = requests.get('https://mcversions.net/').text
    doc = bs4.BeautifulSoup(html, 'html.parser')
    versions = [e.get('id') for e
                in doc.select('.versions div:nth-child(1) .item') if e.get('id')]

    for version in versions:
        print(version, file=sys.stderr)
        link = get_download_link(version)
        if link:
            print(f'{version} {link}')


def get_forge_version(version: str):
    print(version, file=sys.stderr)
    res = requests.get(f'http://files.minecraftforge.net/net/minecraftforge/forge/index_{version}.html')
    print(res.status_code, file=sys.stderr)
    html = res.text
    doc = bs4.BeautifulSoup(html, 'html.parser')
    installer = doc.select_one('.link > a[title=Installer]')
    if installer:
        installer_direct = re.match('.*url=(.*)$', installer.get('href'))[1]
        return installer_direct
    else:
        return None


def get_forge_versions():
    html = requests.get('http://files.minecraftforge.net/').text
    doc = bs4.BeautifulSoup(html, 'html.parser')
    versions = [e.text.strip() for e
                in doc.select('.li-version-list li')]
    for version in versions:
        print(version, file=sys.stderr)
        installer = get_forge_version(version)
        if installer:
            print(f'forge-{version} {installer}\n')


get_versions()
get_forge_versions()
