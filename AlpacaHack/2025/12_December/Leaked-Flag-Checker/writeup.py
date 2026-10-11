"""Leaked Flag Checker

問題url: https://alpacahack.com/challenges/leaked-flag-checker

challenge.cを見ると、以下のようになっている。
1. 入力値とフラグの長さが一致しているかを見る。違ったら"Wrong length"を返す
2. 入力値とフラグの各文字を比較する。違ったら"Wrong at index {idx}"を返す
3. 全て一致したら"Correct"を返す

文字数特定 -> 1文字目から総当たりで文字を特定しにいく。
"""

import string
import subprocess


def challenge_input(input_str) -> str:
    """./challenge にinput_strを入力して、標準出力を返す"""
    result = subprocess.run(
        ["./challenge"], input=input_str, text=True, capture_output=True, check=False
    )
    return result.stdout


def main():
    """main func"""
    # 1. flagの長さを調べる
    flag_length = 1

    for length in range(1, 100):
        print(f"Trying length {length}... ", end="")

        input_str = "x" * length
        output = challenge_input(input_str)
        if "Wrong length" in output:
            print("NG")
        else:
            print("OK")
            flag_length = length
            break

    # 2. flagの各文字を調べる
    flag = "x" * flag_length
    for idx in range(flag_length):
        for ch in string.printable:
            # idx番目の文字をchに置き換えたflagを作る
            test_flag = flag[:idx] + ch + flag[idx + 1 :]

            print(f"Trying flag {test_flag}, index {idx}... ", end="")

            output = challenge_input(test_flag)

            if "Correct" in output:
                print(f"Correct! Flag is {test_flag}")
                flag = test_flag
                break

            wrong_idx = int(output.split()[-1])
            if wrong_idx == idx:
                print("NG")
            else:
                print("OK")
                flag = test_flag
                break

    print(f"Final flag: {flag}")


if __name__ == "__main__":
    main()
