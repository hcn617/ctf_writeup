"""Lucky Redirect
問題url: https://alpacahack.com/daily/challenges/lucky-redirect?month=2026-07

問題文:
    Google 検索の「検索」ボタンは一度も使ったことがありません。
    私には「I'm Feeling Lucky」ボタンだけで十分です。

"""

import requests

# FIXME: "Spawn Challenge Server"ボタンを押して取得したurlをここに貼り付ける
URL = "https://xxx"

UNLUCKY_PATH = "/nope"

flag_path = "A"


while True:
    url = URL + flag_path

    # allow_redirects=False にしないとリダイレクト先に自動で飛ばされる仕様らしい。ChatGPTに教えてもらいました。
    response = requests.get(url, allow_redirects=False, timeout=10)

    location = response.headers.get("Location")
    assert location is not None, "Location header is missing"
    print(location)

    # is_lucky=True のとき、リダイレクト先が新しいパスになる
    if location != UNLUCKY_PATH:
        flag_path = location

    # app.py 21行目
    # return f"Well done! The flag is: {FLAG}
    # とある。これを検出したら出力して終了する
    if "Well done" in response.text:
        print(response.text)
        break
