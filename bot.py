# C:\ProgramData\chocolatey\lib\ngrok\tools
import slack
import os
from pathlib import Path
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
from dotenv import load_dotenv
# from datetime import datetime, timedelta


env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

# client.chat_postMessage(channel="#sub-bot-testing", text="test4")

# @slack_event_adapter.on('message')
# def message(payload):
#     print("Inside message handler")
#     print(payload)
#     event = payload.get('event', {})
#     channel_id = event.get('channel')
#     user_id = event.get('user')
#     text = event.get('text')

#     if BOT_ID != user_id:
#         client.chat_postMessage(channel="#sub-bot-testing", text="test5")
#         client.chat_postMessage(channel=channel_id, text=text)

# messages = [
#     {'text': 'I got the subrequest command!', 'post_at': (datetime.now() + timedelta(seconds=40)).timestamp(), 'channel': }
# ]

@app.route('/subrequest', methods=['POST'])
def sub_request():
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get('channel_id')
    client.chat_postMessage(channel="U05LSGZRL4C", text="I got the subrequest command!")
    return Response(), 200

if __name__ == "__main__":
    app.run(debug=True)