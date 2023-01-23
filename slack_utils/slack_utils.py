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
    A function that sends a message to a slack channel
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
        raise Exception(response.status_code, response.text)


file_name = os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0]
dir_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
if __name__ == "__main__" or __name__ == f"{dir_name}.{file_name}":
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
