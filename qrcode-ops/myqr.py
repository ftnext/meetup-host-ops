import argparse

import qrcode
from more_itertools import batched

Color = tuple[int, int, int]


def calculate_color(code: str) -> Color:
    """
    >>> calculate_color("554171")
    (85, 65, 113)
    """
    assert len(code) == 6
    return tuple(hex_to_int("".join(c)) for c in batched(code, 2))


def hex_to_int(hex: str) -> int:
    return int(hex, 16)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_string")
    parser.add_argument("save_path")
    parser.add_argument("--color", default="554171")
    args = parser.parse_args()

    color = calculate_color(args.color)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(args.data_string)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color="white")
    img.save(args.save_path, format="PNG")
