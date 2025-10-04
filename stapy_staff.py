import argparse
import logging
import os

from hackmd.user_notes import copy_template

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s | %(levelname)s (%(name)s) | %(filename)s:%(funcName)s:%(lineno)d - %(message)s"
        )

    hackmd_token = os.environ["HACKMD_TOKEN"]

    template_note_id = "6LmE8fWeSnyA8aOT78ivrg"
    note_url = copy_template(template_note_id, hackmd_token)
    print(note_url)
