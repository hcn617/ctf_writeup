"""
問題url: https://cryptohack.org/courses/symmetric/ecbcbcwtf/
"""

import requests

ENCRYPT_URL = "https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
DECRYPT_URL = "https://aes.cryptohack.org/ecbcbcwtf/decrypt/{ciphertext}/"


def get_encrypted_flag() -> str:
    """指定されたurlからencrypted_flagを取得する"""
    r = requests.get(ENCRYPT_URL, timeout=10)
    return r.json()["ciphertext"]


def get_decrypted_flag(ciphertext: str) -> str:
    """指定されたurlからdecrypted_flagを取得する"""
    r = requests.get(DECRYPT_URL.format(ciphertext=ciphertext), timeout=10)
    return r.json()["plaintext"]


encrypted_flag = get_encrypted_flag()
iv_hex, ciphertext_hex = encrypted_flag[:32], encrypted_flag[32:]

print(f"{iv_hex=}")
print(f"{ciphertext_hex=}")

decrypted_flag = get_decrypted_flag(ciphertext_hex)
print(f"{decrypted_flag=}")

flag = ""
for i in range(0, len(ciphertext_hex), 32):
    block = ciphertext_hex[i : i + 32]
    decrypted_block = get_decrypted_flag(block)
    now_ans = hex(int(iv_hex, 16) ^ int(decrypted_block, 16))[2:]
    now_ans_bytes = bytes.fromhex(now_ans)
    flag += now_ans_bytes.decode()

    # 次のブロックではこのブロックがIVとして使われる
    iv_hex = block

print(f"{flag=}")
