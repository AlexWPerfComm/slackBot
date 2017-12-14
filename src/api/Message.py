import os
from slackclient import SlackClient

token = os.environ["SLACK_USER_TOKEN"]
sc = SlackClient(token)

list = sc.api_call("conversations.open", users="U0LAVMECR")
print(str(list))
