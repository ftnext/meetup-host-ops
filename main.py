import os

from discord import post_discord
from hackmd import copy_template

if __name__ == "__main__":
    webhook_url = os.environ["DISCORD_WEBHOOK_URL"]
    hackmd_token = os.environ["HACKMD_TOKEN"]

    template_note_id = "1iUWLeIrS7CcluI9xA2tyw"
    team_id = "minodriven-book-pythonista"
    note_url = copy_template(template_note_id, team_id, hackmd_token)
    hackmd_ops_message = f"""🤖HackMDのテンプレートをコピーしました！
{note_url} のTODOの解消だけお願いします🙏"""
    post_discord(hackmd_ops_message, webhook_url)

    connpass_ops_message = """🤖connpassの準備をお願いします。
テンプレート https://connpass.com/event/250267/edit/ をコピーしてTODOを解消し、公開してください"""
    post_discord(connpass_ops_message, webhook_url)
