# redis_utils

A module to send messages to a Slack channel using incoming webhook integration.

## Installation

To install the required packages, run:

pip install -r requirements.txt


## Usage

### `slackMessage`

Sends a message to a Slack channel using incoming webhook integration.

```python
def slackMessage(message: Union[str, Dict], url: str,
                 username: str, symbol: str,
                 title: str = "New Incoming Message :zap:",
                 color: str = "#9733EE"):
    """
    :param message: The message to be sent
    :type message: Union[str, Dict]
    :param url: The url of the Slack channel to post the message
    :type url: str
    :param username: The username of the sender
    :type username: str
    :param symbol: The emoji symbol of the sender
    :type symbol: str
    :param title: The title of the message (default: "New Incoming Message :zap:")
    :type title: str, optional
    :param color: The color of the message (default: "#9733EE")
    :type color: str, optional
    :raises: Exception
    """

```
