# 問題url

https://alpacahack.com/daily/challenges/private-method?month=2026-07

# 問題文

privateなメソッドは呼び出せないはず...


# writeup

pythonは `__` (アンダースコア2つ)をつけてプライベートメソッドみたいに表記することができますが、実は外部からでもアクセスできる雰囲気プライベートメソッドだというお話です。

これが「マングリング」です。

```python
Main.__flag()
```

では呼び出せないけど、

```python
Main._Main__flag()
```

で呼び出せます。メソッドの名前が内部で書き換えられてるだけです。
