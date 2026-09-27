"""
問題url: https://cryptohack.org/courses/symmetric/ecb_oracle/
"""

import time

import requests

ENCRYPT_URL = "https://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext_hex}/"


def encrypt(plaintext_hex: str) -> str:
    """指定されたurlにアクセスして、暗号化された結果を取得する"""
    url = ENCRYPT_URL.format(plaintext_hex=plaintext_hex)
    response = requests.get(url, timeout=10)
    ciphertext_hex = response.json()["ciphertext"]
    return ciphertext_hex


flag = ""
block_idx = 0
while True:
    for i in range(15):
        based_hex = "00" * (15 - i)
        ciphertext_hex = encrypt(based_hex)

        for j in range(256):
            guess_hex = based_hex + flag.encode().hex() + hex(j)[2:].zfill(2)
            guess_ciphertext_hex = encrypt(guess_hex)
            li, ri = 32 * block_idx, 32 * (block_idx + 1)
            if guess_ciphertext_hex[li:ri] == ciphertext_hex[li:ri]:
                flag += chr(j)
                print(time.strftime("%Y-%m-%d %H:%M:%S"), f"{chr(j)=}, {flag=}")
                break
        if flag.endswith("}"):
            break
    if flag.endswith("}"):
        break

    # 上の処理だと16文字目はbased_hexが空文字になってしまいエラーになるため、ここだけ処理を分ける
    based_hex = "00" * 16
    ciphertext_hex = encrypt(based_hex)
    for j in range(256):
        guess_hex = based_hex + flag.encode().hex() + hex(j)[2:].zfill(2)
        guess_ciphertext_hex = encrypt(guess_hex)
        li, ri = 32 * (block_idx + 1), 32 * (block_idx + 2)
        if guess_ciphertext_hex[li:ri] == ciphertext_hex[li:ri]:
            flag += chr(j)
            print(time.strftime("%Y-%m-%d %H:%M:%S"), f"{chr(j)=}, {flag=}")
            break
    if flag.endswith("}"):
        break

    block_idx += 1

print(f"{flag=}")
