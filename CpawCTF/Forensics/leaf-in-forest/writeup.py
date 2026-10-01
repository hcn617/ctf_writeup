"""
問題url: https://ctf.cpaw.site/questions.php?qnum=18

writeup:
    ファイルを開けてみると、かなりの"lovelive!"の文字列が並んでいる。
    スクロールしていると、"WWW"という文字列が紛れているのを見つけた。
    文字列を全コピーして、misc.txtとして保存。
    "lovelive"に含まれる文字を全て取り除くと、フラグが現れた。
"""

with open("misc.txt", "r") as f:
    text = f.read()
    for ch in "lovelive!":
        text = text.replace(ch, "")
    text = text[5:]  # 最初の"ﾔﾃｲ｡％"を消しているだけ
    print(text)
