import argparse
import os
from dataclasses import dataclass

from client import api_post

BitlinkUrl = str


@dataclass
class Bitlink:
    id: str
    link: BitlinkUrl


def shorten(long_url: str, token: str) -> Bitlink:
    endpoint = "https://api-ssl.bitly.com/v4/shorten"
    data = {"long_url": long_url}
    response = api_post(endpoint, data, token)
    return Bitlink(response["id"], response["link"])


def customize(bitlink_id: str, custom_slug: str, token: str) -> BitlinkUrl:
    endpoint = "https://api-ssl.bitly.com/v4/custom_bitlinks"
    data = {
        "bitlink_id": bitlink_id,
        "custom_bitlink": f"bit.ly/{custom_slug}",
    }
    response = api_post(endpoint, data, token)
    return response["bitlink"]["custom_bitlinks"][0]


def main(long_url: str, custom_slug: str, token: str) -> BitlinkUrl:
    short_url = shorten(long_url, token)
    return customize(short_url.id, custom_slug, token)


if __name__ == "__main__":
    bitly_token = os.environ["BITLY_ACCESS_TOKEN"]

    parser = argparse.ArgumentParser()
    parser.add_argument("long_url")
    parser.add_argument("custom_slug")
    args = parser.parse_args()

    short_url = main(args.long_url, args.custom_slug, bitly_token)
    print(f"Created: {short_url}")
