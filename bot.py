# C:\ProgramData\chocolatey\lib\ngrok\tools
import slack_sdk
import os
from pathlib import Path
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
from dotenv import load_dotenv

# from datetime import datetime, timedelta
# messages = [
#     {'text': 'I got the subrequest command!', 'post_at': (datetime.now() + timedelta(seconds=40)).timestamp(), 'channel': }
# ]


env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)


client = slack_sdk.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']
teachers = ['U05LSGZRL4C']


@app.route('/subrequest', methods=['POST'])
def sub_request():
    # data = request.form
    #user_id = data.get('user_id')
    #channel_id = data.get('channel_id')
    for teacher in teachers:   
        client.chat_postMessage(channel=teacher, text="I need a sub!")
    return Response(), 200


# @slack_event_adapter.on('message')
# def message(payload):
#     print("Inside message handler")
#     print(payload)
#     event = payload.get('event', {})
#     channel_id = event.get('channel')
#     user_id = event.get('user')
#     text = event.get('text')


#     if user_id != None and BOT_ID != user_id:
#         client.chat_postMessage(channel=channel_id, text='testing')


if __name__ == "__main__":
    app.run(debug=True)