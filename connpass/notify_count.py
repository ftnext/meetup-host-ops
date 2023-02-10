from datetime import datetime
import json
import os
from urllib import parse, request

# ref: https://connpass.com/about/api/
# https://connpass.com/api/v1/event/?event_id=159691
EVENT_ID = '159691'
BOT_TOKEN = os.getenv('BOT_USER_OAUTH_TOKEN')


def return_connpass_url_of_specified_event(event_id):
    queries = {'event_id': event_id}
    params = parse.urlencode(queries)
    return f'https://connpass.com/api/v1/event/?{params}'


def request_connpass_api(url):
    with request.urlopen(url) as f:
        return f.read().decode('utf-8')


def select_event_info(response_dict, event_id):
    event_info = None
    for result_event in response_dict['events']:
        if result_event['event_id'] == int(event_id):
            event_info = result_event
    return event_info


def return_notify_message(event_info, executed_datetime):
    title = event_info['title']
    limit = event_info['limit']
    accepted = event_info['accepted']
    waiting = event_info['waiting']

    notify_sentence = f'''\
    「{title}」の申込者数({executed_datetime:%m/%d %H時}時点)：
    参加者数 {accepted}名'''
    if waiting:
        notify_sentence += f' (補欠 {waiting}名)'
    
    return notify_sentence


def post_slack(channel, message):
    slack_url = 'https://slack.com/api/chat.postMessage'
    data = {
        'channel': channel,
        'text': message
    }
    jsoned = json.dumps(data).encode('utf-8')
    headers = {
        'Authorization': f"Bearer {BOT_TOKEN}",
        'Content-type': 'application/json'
    }
    req = request.Request(slack_url, data=jsoned, method='POST', headers=headers)
    request.urlopen(req)


def main_handler(event, context):
    now = datetime.now()
    url = return_connpass_url_of_specified_event(EVENT_ID)
    response_str = request_connpass_api(url)
    result = json.loads(response_str)
    event_info = select_event_info(result, EVENT_ID)
    assert event_info, f'event_id:{EVENT_ID}に該当するイベントが見つかりません'
    message = return_notify_message(event_info, now)
    post_slack('運営', message)


if __name__ == '__main__':
    main_handler(None, None)
