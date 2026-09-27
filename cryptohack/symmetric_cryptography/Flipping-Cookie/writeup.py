"""
問題url: https://cryptohack.org/courses/symmetric/flipping_cookie/
"""

import requests

GET_COOKIE_URL = "https://aes.cryptohack.org/flipping_cookie/get_cookie/"
CHECK_ADMIN_URL = (
    "https://aes.cryptohack.org/flipping_cookie/check_admin/{cookie}/{iv}/"
)


def get_cookie() -> str:
    """指定されたurlからcookieを取得する"""
    r = requests.get(GET_COOKIE_URL, timeout=10)
    return r.json()["cookie"]


def check_admin(cookie: str, iv: str) -> tuple[bool, str] | None:
    """指定されたcookieとivで管理者権限をチェックする

    管理者権限あり: Trueを返す
    管理者権限なし: Falseを返す
    エラーなどその他の場合: Noneを返す
    """
    r = requests.get(CHECK_ADMIN_URL.format(cookie=cookie, iv=iv), timeout=10)
    r_json = r.json()
    if "flag" in r_json:
        return True, r_json["flag"]
    if r_json.get("error") == "Only admin can read the flag":
        return False, r_json.get("error")
    return None


cookie = get_cookie()
iv_hex, encrypted_flag_hex = cookie[:32], cookie[32:]


cookie_first_block = b"admin=False;expi"
new_cookie_first_block = b"admin=True;expir"
assert len(cookie_first_block) == len(new_cookie_first_block) == 16


iv = bytes.fromhex(iv_hex)
new_iv_hex = bytes(
    a ^ b ^ c for a, b, c in zip(iv, cookie_first_block, new_cookie_first_block)
).hex()


res = check_admin(cookie=encrypted_flag_hex, iv=new_iv_hex)
print(f"{res=}")
