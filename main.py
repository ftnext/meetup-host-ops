import os

from discord import post_discord

if __name__ == "__main__":
    webhook_url = os.environ["DISCORD_WEBHOOK_URL"]

    hackmd_ops_message = """🤖HackMDの準備をお願いします。
テンプレート https://hackmd.io/dHiRbfcKTj68SY9p9dYfnw をコピーしてTODOを解消してください"""
    post_discord(hackmd_ops_message, webhook_url)

    connpass_ops_message = """🤖connpassの準備をお願いします。
テンプレート https://connpass.com/event/250267/edit/ をコピーしてTODOを解消し、公開してください"""
    post_discord(connpass_ops_message, webhook_url)
