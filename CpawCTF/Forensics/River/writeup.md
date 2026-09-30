# 問題url

https://ctf.cpaw.site/questions.php?qnum=10

# 問題文

JPEGという画像ファイルのフォーマットでは、撮影時の日時、使われたカメラ、位置情報など様々な情報(Exif情報)が付加されることがあるらしい。
この情報から、写真に写っている川の名前を特定して欲しい。

# writeup

```bash
(venv) ~/ctf% exiftool river.jpg
```

出力結果
```bash
# (長いので中略)

GPS Position                    : 31 deg 35' 2.76" N, 130 deg 32' 51.73" E
```

Googleマップでは、緯度経度でも検索できるらしい。

公式ヘルプ: 
https://support.google.com/maps/answer/18539?hl=ja&co=GENIE.Platform%3DDesktop

`cpaw{調べて出てきた川の名前}` をsubmitしてACできました。
