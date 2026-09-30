"""
問題url: https://ctf.cpaw.site/questions.php?qnum=12

writeup:
    https://crackstation.net/ でハッシュを解読した。
    一応手元でも一致しているのを確認してsubmitです。
"""

import hashlib

FLAG = "Shal"  # crackstationで解読したもの
HASHED_VALUE = "e4c6bced9edff99746401bd077afa92860f83de3"

print(hashlib.sha1(FLAG.encode()).hexdigest() == HASHED_VALUE)  # True
