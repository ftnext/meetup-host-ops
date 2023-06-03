import json
from urllib.request import Request, urlopen


def api_get(url, token):
    headers = {"Authorization": f"Bearer {token}"}
    request = Request(url, headers=headers)

    with urlopen(request) as res:
        return json.load(res)


def api_post(url, data, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    request = Request(url, data=json.dumps(data).encode(), headers=headers)
    with urlopen(request) as res:
        return json.load(res)
