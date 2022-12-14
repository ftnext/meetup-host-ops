import os

from discord import post_discord
from hackmd import copy_template

if __name__ == "__main__":
    webhook_url = os.environ["DISCORD_WEBHOOK_URL"]
    hackmd_token = os.environ["HACKMD_TOKEN"]

    template_note_id = "1iUWLeIrS7CcluI9xA2tyw"
    team_id = "minodriven-book-pythonista"
    note_url = copy_template(template_note_id, team_id, hackmd_token)
    hackmd_ops_message = f"""ð¤HackMDã®ãã³ãã¬ã¼ããã³ãã¼ãã¾ããï¼
{note_url} ã®TODOã®è§£æ¶ã ããé¡ããã¾ãð"""
    post_discord(hackmd_ops_message, webhook_url)

    connpass_ops_message = """ð¤connpassã®æºåããé¡ããã¾ãã
ãã³ãã¬ã¼ã https://connpass.com/event/250267/edit/ ãã³ãã¼ãã¦TODOãè§£æ¶ããå¬éãã¦ãã ãã"""
    post_discord(connpass_ops_message, webhook_url)
