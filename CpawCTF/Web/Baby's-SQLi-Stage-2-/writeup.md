# 問題url

https://ctf.cpaw.site/questions.php?qnum=24

# 問題文

うーん，ぱろっく先生深くまで逃げ込んでたか．
そこまで難しくは無いと思うんだけども……．

えっ？何の話か分からない？
さてはStage 1をクリアしてないな．
待っているから，先にStage 1をクリアしてからもう一度来てね．

# writeup

stage1のurl: https://ctf.cpaw.site/questions.php?qnum=22

もしもバックエンド側で
```python
sql = "COUNT(*) FROM users WHERE username='" + username + "' AND hashed_password='" + hashed_password + "';"
```

みたいに文字列の結合をしてsqlを生成していたとき、

ユーザー名: `porisuteru' OR 1=1; --`
パスワード: `something`

にすると、

```sql
COUNT(*)
FROM users 
WHERE username='porisuteru' 
    OR 1=1; --' AND hashed_password='hashed_something';
```

となる。

`OR 1=1` 部分のせいで必ずWHERE句がTrueになり、後ろのパスワード解析部分はコメントアウトさせられて全滅しているので、ログインが成功してしまう。
