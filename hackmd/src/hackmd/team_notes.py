from hackmd.client import api_post
from hackmd.user_notes import get_contents


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
