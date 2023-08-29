import argparse
import base64
import os

from client import api_get, api_post


def get_bitly_id(slug, token):
    response = api_get(
        f"https://api-ssl.bitly.com/v4/bitlinks/bit.ly/{slug}", token
    )
    return response["id"]


def create_qr_code(bitly_id, token):
    response = api_post(
        f"https://api-ssl.bitly.com/v4/bitlinks/{bitly_id}/qr",
        {"image_format": "png"},
        token,
    )
    return response["qr_code"].removeprefix("data:image/png;base64,")


def get_qr_code(bitly_id, token):
    response = api_get(
        f"https://api-ssl.bitly.com/v4/bitlinks/{bitly_id}/qr?image_format=png",
        token,
    )
    return response["qr_code"].removeprefix("data:image/png;base64,")


def save_qr_code(qr_code, path):
    with open(path, "wb") as fb:
        fb.write(base64.b64decode(qr_code))


def create_command(args):
    bitly_token = os.environ["BITLY_ACCESS_TOKEN"]
    bitly_id = get_bitly_id(args.custom_slug, bitly_token)
    qr_code_bytes = create_qr_code(bitly_id, bitly_token)
    save_qr_code(qr_code_bytes, args.qr_code_save_path)


def get_command(args):
    bitly_token = os.environ["BITLY_ACCESS_TOKEN"]
    bitly_id = get_bitly_id(args.custom_slug, bitly_token)
    qr_code_bytes = get_qr_code(bitly_id, bitly_token)
    save_qr_code(qr_code_bytes, args.qr_code_save_path)


if __name__ == "__main__":
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument("custom_slug")
    parent_parser.add_argument("qr_code_save_path")

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    create_parser = subparsers.add_parser("create", parents=[parent_parser])
    create_parser.set_defaults(func=create_command)

    get_parser = subparsers.add_parser("get", parents=[parent_parser])
    get_parser.set_defaults(func=get_command)

    args = parser.parse_args()
    args.func(args)
