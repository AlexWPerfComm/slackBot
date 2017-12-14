import requests
import json

def getQuote():
    r = requests.get('http://shitballs.life/rest/api/phrase')
    j = json.loads(r.text)
    return j[0]['content']
