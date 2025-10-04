from hackmd.client import api_get, api_post


def get_contents(note_id, token):
    endpoint = f"https://api.hackmd.io/v1/notes/{note_id}"
    return api_get(endpoint, token)


def create_user_note(title, content, token):
    endpoint = f"https://api.hackmd.io/v1/notes"
    data = {
        "title": title,
        "content": content,
        "readPermission": "signed_in",
        "writePermission": "signed_in",
    }
    response = api_post(endpoint, data, token)
    return f'https://hackmd.io/{response["note"]["id"]}'


def copy_template(template_id, token):
    template_contents = get_contents(template_id, token)

    title = f'Copy of {template_contents["title"]}'
    content = template_contents["content"]

    copied_url = create_user_note(title, content, token)
    return copied_url
