"""duplicate entry

問題url: https://alpacahack.com/daily/challenges/duplicate-entry?month=2026-07
"""

import zipfile

ZIP_PATH = "ctf/flag.zip"  # FIXME: flag.zipのパスにしてください

with zipfile.ZipFile(ZIP_PATH) as zf:
    for info in zf.infolist():
        with zf.open(info) as f:
            text = f.read().decode("utf-8")
            if "Alpaca" in text:
                print(text)
