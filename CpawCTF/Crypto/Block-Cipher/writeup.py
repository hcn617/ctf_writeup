"""
問題url: https://ctf.cpaw.site/questions.php?qnum=20

writeup:
    C言語の環境がないので、「C言語 playground」で検索してヒットした以下のページを拝借
    https://cplayground.com/?p=otter-mole-dogfish
    key=4, flag="abcdefg" として実行すると、"dcbagfe" が返ってきた。
    4文字目に大文字のYがあって、おそらくkey=4だと推測。もし違ったらfor文でkeyの値を回してくつもりでした。
    pythonでこれの復元バージョンを書いてACできました。

"""

CIPHERTEXT = "ruoYced_ehpigniriks_i_llrg_stae"
KEY = 4
for i in range(KEY - 1, len(CIPHERTEXT), KEY):
    for j in range(i, i - KEY, -1):
        print(CIPHERTEXT[j], end="")

if len(CIPHERTEXT) % KEY != 0:
    for i in range(
        len(CIPHERTEXT) - 1, len(CIPHERTEXT) - len(CIPHERTEXT) % KEY - 1, -1
    ):
        print(CIPHERTEXT[i], end="")
