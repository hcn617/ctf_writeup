"""
問題url: https://cryptohack.org/courses/symmetric/passwords_as_keys/
"""

import hashlib

import requests
from Crypto.Cipher import AES

CIPHERTEXT_URL = "https://aes.cryptohack.org/passwords_as_keys/encrypt_flag/"
WORDS_URL = "https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words"


def get_ciphertext() -> str:
    """指定されたurlからciphertextを取得する"""
    response = requests.get(CIPHERTEXT_URL, timeout=10)
    ciphertext = response.json()["ciphertext"]
    return ciphertext


def get_keys() -> list[bytes]:
    """指定されたurlからpassword_hashのリストを取得する"""
    response = requests.get(WORDS_URL, timeout=10)
    words_list = response.text.splitlines()
    keys = [hashlib.md5(word.encode()).digest() for word in words_list]

    return keys


def decrypt(ciphertext: str, key: bytes) -> bytes | None:
    """問題文にあるdecrypt関数を少し改変したもの"""
    ciphertext_bytes = bytes.fromhex(ciphertext)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext_bytes)
    except ValueError as _e:
        return None

    return decrypted


if __name__ == "__main__":
    ciphertext = get_ciphertext()
    keys = get_keys()

    for key in keys:
        plaintext = decrypt(ciphertext, key)
        if plaintext is not None and plaintext.startswith(b"crypto{"):
            print(plaintext)
