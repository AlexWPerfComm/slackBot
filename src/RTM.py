import os
import time
from api import Shitballs
from slackclient import SlackClient

slack_token = os.environ["SLACK_USER_TOKEN"]
sc = SlackClient(slack_token)

if sc.rtm_connect(with_team_state=False):
    while True:
        p = sc.rtm_read()
        if len(p) > 0:
            try:
                r = ""
                print(p[0]['type'])
                if p[0]['type'] == 'message':
                    m = p[0]['text'].lower()
                    if m == 'ping':
                        r = "pong"
                    if m == 'shitballs':
                        r = Shitballs.getQuote()
                if r != "":
                    sc.rtm_send_message(p[0]['channel'], r)
            except:
                print(str(p))
        time.sleep(1)
else:
    print("Connection Failed")
