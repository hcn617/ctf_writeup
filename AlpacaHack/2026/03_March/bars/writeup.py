"""bars

問題url: https://alpacahack.com/challenges/bars
"""

import requests

URL = "http://34.170.146.252:57550/"  # FIXME: challenge server url

res = requests.get(URL, timeout=10)
print(res.text)
