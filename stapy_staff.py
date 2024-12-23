import os

from hackmd.user_notes import copy_template

if __name__ == "__main__":
    hackmd_token = os.environ["HACKMD_TOKEN"]

    template_note_id = "6LmE8fWeSnyA8aOT78ivrg"
    note_url = copy_template(template_note_id, hackmd_token)
    print(note_url)
