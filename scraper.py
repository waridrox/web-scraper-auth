import os
import json
import requests
from bs4 import BeautifulSoup

data = {
'commit': 'Sign in',
'authenticity_token': os.environ.get('AUTH_TOKEN'),
'login': os.environ.get('LOGIN_EMAIL'),
'password': os.environ.get('LOGIN_EMAIL_PASS'),
'trusted_device': '',
'webauthn-support': 'supported',
'webauthn-iuvpaa-support': 'unsupported',
'return_to': '/issues?q=is%3Aissue+user%3Amoja-global+label%3A%22good+first+issue%22+is%3Aopen',
'allow_signup': '',
'client_id': '',
'integration': '',
'required_field_8124': '',
'timestamp': '1620255824865',
'timestamp_secret': '7a43008bae2ae827eb3e0b3070564202ecc17830b2d994dc5ba8bee78cc40b76'
}

cookies = {
    'cookie': '_octo=GH1.1.1501040068.1620255466; logged_in=no; tz=Asia%2FCalcutta; _device_id=1922e2c8d06e51fcef880dc5c9e058ac; _gh_sess=OsGth2hBnxJLQVYn75ilfhnJ9BvwLxiNT7Eg3kKWql4hl5RJk2H7hhNwomlcjZRVhNhGzkaoQSJpxnKcWbGdeSbqXQ3Z4fmnsQFqhR59TAf1wnixLCzOLOl4K9RMn8WSyoSjbHStiytQljpNXXFbxbE%2FF4B8FZ5XpH2jH6YxJNo%2FKnDL2DT7UJuHC151e9NH2XNLo2OlUdW1Hr33x6l7candUGtNEUa4BDNnvGiQfT6HVuh0uyESyPtDLfKZFTxTb1KQbYrBDQYuFU75Wud35pRS1QUvvy5IeM7zdpjQ9a6mF9KXRIv4vI2UDx7AdsLNzJ7XoAkGsbJYEUrL16Gvs%2BxwTIlF9pc1kKb1xLsr3g%2FWQpl%2By%2BGC8W0r1nvr9Qsqu5LGV%2FfDRI2TwluzOGSElgL7mKILPlJI7pgw23SWdc12dWrMOAOLfRIanqLYQALR5MsavOd2yYINoNc0HQ7cSUraXiE%2FhT2DKJ04tDW6eT8wnwqNKgzWspc4VD4kZ5jlFZhjpBOF6B5omC80%2F9KKD%2FqpENsgXSB6KXKhmuCmYtrVeiWxVyraN%2BRHUmFkOFDpP0c8j0dP7x%2FHV%2B5AFNlhAs5sdk05aMPL071mXeZTUgWooOyh9KfUYG9YPV7BUx5V3D8J0b8xPkmacFxn0JT71bl87M8yLluy7JminyOTPdMRLxCQNwjC7NSPc3YLB1rl--vOL4tl9Mnea1tXc1--cRHrFjvjw63YeHVHVGkpvw%3D%3D',
}

url = "https://github.com/session"

s = requests.Session()
s.post(url, data=data, cookies=cookies)
result = s.get("https://github.com/issues?q=is%3Aissue+user%3Amoja-global+label%3A%22good+first+issue%22+is%3Aopen")
content = result.content

soup = BeautifulSoup(content, features="lxml")

repos = list(set(((str(i.get_text()))[23:]).rstrip("\n") for i in soup.find_all("a", class_="v-align-middle Link--muted h4 pr-1")))

# exporting the DATA TO A JSON FILE
json.dumps({'repos': repos})

with open('RepoNames.json', 'w') as f:
  json.dump(repos, f)
#JSON object is now saved