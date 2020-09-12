import re
from sys import version
import requests
import bs4
from requests.api import request


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
        link = get_download_link(version)
        if link:
            with open('versions.txt', 'at', encoding='utf-8') as f:
                f.write(f'{version} {link}\n')


def get_forge_version(version: str):
    html = requests.get(f'http://files.minecraftforge.net/maven/net/minecraftforge/forge/index_{version}.html').text
    doc = bs4.BeautifulSoup(html, 'html.parser')
    latest = doc.select_one('.link > a[title=Installer]')
    if latest:
        direct = re.match('.*url=(.*)$', latest.get('href'))[1]
        return direct


def get_forge_versions():
    html = requests.get('http://files.minecraftforge.net/').text
    doc = bs4.BeautifulSoup(html, 'html.parser')
    versions = [e.text.strip() for e
                in doc.select('.li-version-list li')]
    for version in versions:
        link = get_forge_version(version)
        if link:
            with open('versions.txt', 'at', encoding='utf-8') as f:
                f.write(f'forge-{version} {link}\n')


get_versions()
get_forge_versions()
