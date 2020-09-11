from sys import version
import requests
import bs4


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

    with open('versions.txt', 'wt', encoding='utf-8') as f:
        for version in versions:
            link = get_download_link(version)
            if link:
                f.write(f'{version} {link}\n')


get_versions()
