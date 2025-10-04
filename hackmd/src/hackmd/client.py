import json
import logging
from urllib.request import Request, urlopen

logger = logging.getLogger(__name__)


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
    logger.debug("POST %s %s", url, data)

    request = Request(url, data=json.dumps(data).encode(), headers=headers)
    with urlopen(request) as res:
        response = json.load(res)

    logger.debug("Response: %s", response)
    return response
