# slack_utils

A module to send messages to a Slack channel using incoming webhook integration.

Slack is a cloud-based team collaboration platform that is widely used in businesses and organizations of all sizes. It provides a range of features to facilitate communication and collaboration among team members, including real-time messaging, voice and video calls, file sharing, and integrations with other tools and services.

Slack allows team members to communicate and collaborate in a single platform, reducing the need for multiple tools and channels of communication. Users can create channels for specific projects or teams, and can invite other team members to join these channels. They can also send direct messages to individual team members or groups of team members.

Slack also provides a range of integrations with other tools and services, such as project management tools, customer relationship management (CRM) software, and social media platforms. These integrations allow team members to access and share information from other tools and services directly within Slack.

In addition to its core messaging and collaboration features, Slack provides a range of tools to manage teams and projects, including the ability to set reminders, create polls, and track tasks and deadlines. Slack also provides analytics and reporting tools to help teams monitor their activity and performance.

Slack can be accessed through a web interface or through its desktop and mobile apps, and is available on multiple platforms, including Windows, macOS, iOS, and Android.

Overall, Slack is a powerful tool for team collaboration and communication, and is widely used by businesses and organizations of all sizes to improve productivity, efficiency, and collaboration among team members.

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
