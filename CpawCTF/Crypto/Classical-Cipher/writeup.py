"""
問題url: https://ctf.cpaw.site/questions.php?qnum=6
"""

ciphertext = "fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}"

ans = ""
for c in ciphertext:
    if c.isalpha():
        ans += chr(ord(c) - 3)
    else:
        ans += c
print(ans)
