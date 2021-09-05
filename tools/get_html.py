import sys
import requests
import os
import urllib.parse
import urllib.robotparser
import json
import time


def check_robots_txt(url, user_agent='mytestbot'):
    '''
    robots.txtを確認
    '''
    parse_result = urllib.parse.urlparse(url)
    robots_url = f'{parse_result.scheme}://{parse_result.netloc}/robots.txt'
    if url == robots_url:
        return True
    else:
        source = get_html(robots_url)

    parser = urllib.robotparser.RobotFileParser()
    parser.parse(source.split('\n'))
    return parser.can_fetch(user_agent, url)


def take_domain_interval(url, interval=5):
    '''
    同一サーバへのアクセスに間隔を開ける関数
    '''
    filename = 'domains.json'
    parse_result = urllib.parse.urlparse(url)
    domain = parse_result.netloc

    # 保存された最終アクセス時刻を読み込む
    if os.path.exists(filename):
        try:
            with open(filename, 'rt', encoding='utf-8') as f:
                interval_table = json.load(f)
        except:
            interval_table = dict()
    else:
        interval_table = dict()

    # 最終アクセス時刻から少なくともinterval秒待つ
    if domain in interval_table:
        wait_time = interval - (time.time() - interval_table[domain])
        if wait_time > 0:
            print(f'taking interval...{wait_time:.1f}s', file=sys.stderr)
            time.sleep(wait_time)

    # 最終アクセス時刻を更新する
    interval_table[domain] = time.time()
    with open(filename, 'wt', encoding='utf-8') as f:
        json.dump(interval_table, f, indent=4)


def get_html(url):
    '''
    行儀の良いHTML取得関数
    '''
    # キャッシュの場所
    cachedir = 'cache'
    os.makedirs(cachedir, exist_ok=True)
    # URLそのままではファイル名に使えない文字が含まれているので、
    # パーセント記法というものに置き換える
    cachefile = urllib.parse.quote(url, safe='') + '.html'
    cachepath = os.path.join(cachedir, cachefile)

    if os.path.exists(cachepath):
        # キャッシュが存在した場合にはそれを読み取る
        with open(cachepath, 'rt', encoding='utf-8') as f:
            html = f.read()
    else:
        # キャッシュが存在しないならリクエストを送る
        # robots.txtの確認
        if not check_robots_txt(url):
            # robots.txtで禁止されてる
            print('forbidden by robots.txt', file=sys.stderr)
            exit(1)

        print('do request:', url, file=sys.stderr)
        # アクセス間隔の確保
        take_domain_interval(url)
        # リクエスト実行
        html = requests.get(url).text
        # キャッシュを保存
        with open(cachepath, 'wt', encoding='utf-8') as f:
            f.write(html)

    return html
