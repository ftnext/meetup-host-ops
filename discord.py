import requests


def post_discord(message: str, webhook_url: str):
    data = {"content": message}
    res = requests.post(webhook_url, json=data)
    assert res.status_code == 204
