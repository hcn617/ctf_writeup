"""Encoding Basics

問題url: https://alpacahack.com/challenges/encoding-basics
"""

import base64

from Crypto.Util.number import *

# chall.txt
long_value = 373502670300504551747111047082539140193958649718
hex_string = "346c5f6833785f6630726d61745f31735f636c33"
base64_string = "NG5fYjY0X3A0ZGQxbmdfaXNfY29vbH0="


flag1 = long_to_bytes(long_value).decode()
flag2 = bytes.fromhex(hex_string).decode()
flag3 = base64.b64decode(base64_string).decode()

print(f"{flag1=}")
print(f"{flag2=}")
print(f"{flag3=}")

flag = flag1 + flag2 + flag3
print(f"{flag=}")
