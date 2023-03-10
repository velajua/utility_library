import os
import sys
import json
import requests

from typing import Dict, Union


def slackMessage(message: Union[str, Dict], url: str,
                 username: str, symbol: str,
                 title: str = "New Incoming Message :zap:",
                 color: str = "#9733EE"):
    """
    A function that sends a message to a slack channel using the
      url from the incoming webhook integration 
    :param message: The message to be sent
    :type message: Union[str, Dict]
    :param url: The url of the slack channel to post the message
    :type url: str
    :param username: The username of the sender
    :type username: str
    :param symbol: The emoji symbol of the sender
    :type symbol: str
    :param title: The title of the message
    :type title: str
    :param color: The color of the message
    :type color: str
    :raises: Exception
    """
    slack_data = {
        "username": username,
        "icon_emoji": symbol,
        "attachments": [
            {
                "color": color,
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "False",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json",
               'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data),
                             headers=headers)
    if response.status_code != 200:
        return ('Error', response.status_code, response.text)


def send_message(channel: str, text: str,
                 TOKEN: str = None) -> str:
    """
    Sends a message to a Slack channel using the Slack Web API.
    follow: https://www.pragnakalp.com/
create-slack-bot-using-python-tutorial-with-examples/
    for steps.

    Parameters:
    - channel (str): the name or ID of the
        channel to send the message to.
    - text (str): the message text to send.
    - TOKEN (str): the Bot User OAuth Access
        Token for your Slack app (required).

    Returns:
    - A string representation of the JSON
        response from the Slack API.

    Example usage:
    ```
    TOKEN = "your-token"
    send_message(channel="general",
                 text="Hello from Python!", TOKEN=TOKEN)
    ```
    """
    if not TOKEN:
        return "Error: No Slack token provided."
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer {}".format(TOKEN),
    }
    json = {"channel": channel, "text": text}
    typing_url = "https://slack.com/api/chat.postMessage"
    typing_json = {
        "channel": channel,
        "text": "",
        "blocks": [{"type": "section",
                    "text": {"type": "mrkdwn", "text": "Typing..."}}],
    }
    requests.post(url=typing_url, headers=headers, json=typing_json)
    response = requests.post(url=url, headers=headers, json=json)
    return response.text


file_name = os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0]
dir_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
if __name__ == "__main__" or __name__ == f"{dir_name}.{file_name}":
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
