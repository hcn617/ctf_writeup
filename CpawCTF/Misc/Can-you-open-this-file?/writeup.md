# 問題url

http://ctf.cpaw.site/questions.php?qnum=8

# 問題文

このファイルを開きたいが拡張子がないので、どのような種類のファイルで、どのアプリケーションで開けば良いかわからない。
どうにかして、この拡張子がないこのファイルの種類を特定し、どのアプリケーションで開くか調べてくれ。

# writeup

ファイルの種類を特定する
```bash
(venv) ~/ctf% file open_me 
```

出力結果
```bash
open_me: Composite Document File V2 Document, Little Endian, Os: Windows, Version 10.0, Code page: 932, Author: �v��, Template: Normal.dotm, Last Saved By: �v��, Revision Number: 1, Name of Creating Application: Microsoft Office Word, Total Editing Time: 28:00, Create Time/Date: Mon Oct 12 04:27:00 2015, Last Saved Time/Date: Mon Oct 12 04:55:00 2015, Number of Pages: 1, Number of Words: 3, Number of Characters: 23, Security: 0
```

-> `Application: Microsoft Office Word` と書いてある。

残念ながら私のパソコンにはMicrosoftさんのWordは入っていないので、Googleさんの力を借りてGoogleドライブにアップしてGoogleドキュメントで見に行った。

flagが書いてある画像が貼り付けられていた。

スクリーンショットを撮って、その画像の中の文字列部分をダブルクリックすると、文字列として認識してコピペできる。macのpcだけなのかな。便利。


