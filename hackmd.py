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
