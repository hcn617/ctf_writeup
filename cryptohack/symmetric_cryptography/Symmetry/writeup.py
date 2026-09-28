"""
問題url: https://cryptohack.org/courses/symmetric/symmetry/
"""

import requests

ENCRYPT_FLAG_URL = "https://aes.cryptohack.org/symmetry/encrypt_flag/"
ENCRYPT_URL = "https://aes.cryptohack.org/symmetry/encrypt/{plaintext}/{iv}"


def encrypt_flag() -> str:
    """指定されたurlから暗号化されたフラグを取得する"""
    r = requests.get(ENCRYPT_FLAG_URL, timeout=10)
    return r.json()["ciphertext"]


def encrypt(plaintext: str, iv: str) -> str:
    """指定されたurlから暗号化されたテキストを取得する"""
    r = requests.get(ENCRYPT_URL.format(plaintext=plaintext, iv=iv), timeout=10)
    return r.json()["ciphertext"]


ciphertext = encrypt_flag()
iv_hex, encrypted_hex = ciphertext[:32], ciphertext[32:]

dummy_hex = "0" * len(encrypted_hex)
my_ciphertext = encrypt(dummy_hex, iv_hex)
key_int = int(my_ciphertext, 16) ^ int(dummy_hex, 16)

decrypted_int = int(encrypted_hex, 16) ^ key_int
decrypted_hex = hex(decrypted_int)[2:].zfill(len(encrypted_hex))
decrypted_flag = bytes.fromhex(decrypted_hex)

print(decrypted_flag)
