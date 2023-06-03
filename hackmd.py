from client import api_get, api_post


def get_contents(note_id, token):
    endpoint = f"https://api.hackmd.io/v1/notes/{note_id}"
    return api_get(endpoint, token)


def create_team_note(title, content, team_id, token):
    endpoint = f"https://api.hackmd.io/v1/teams/{team_id}/notes"
    data = {
        "title": title,
        "content": content,
        "readPermission": "guest",
        "writePermission": "signed_in",
    }
    response = api_post(endpoint, data, token)
    return f'https://hackmd.io/{response["id"]}'


def copy_template(template_id, team_id, token):
    template_contents = get_contents(template_id, token)

    title = f'Copy of {template_contents["title"]}'
    content = template_contents["content"]

    copied_url = create_team_note(title, content, team_id, token)
    return copied_url
