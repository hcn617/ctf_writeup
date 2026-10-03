"""Renda

問題url: https://alpacahack.com/daily/challenges/renda?month=2026-07

問題文: 連打するだけ!

Note: 
    pyautogui documentation: https://pyautogui.readthedocs.io/en/latest/index.html
    たくさんクリックするときは、clicks引数を使う (参考url: https://pyautogui.readthedocs.io/en/latest/mouse.html)

    for _ in range(100_000): pyautogui.click() だとめちゃくちゃ時間かかります。
    どれくらい時間かかりそうか分からないし、まず100回くらいでお試ししてから本番のクリック回数に進むと良かった。。
"""

import time

import pyautogui

SLEEP_TIME = 10
CLICK_COUNT = 100_000

# 少し待つ
time.sleep(SLEEP_TIME)

# 100_000回クリックする
pyautogui.click(clicks=CLICK_COUNT)
