import requests
import pandas
import json

def pageToken():
    # the url to pass to our request
    the_url = 'https://graph.facebook.com/me/accounts'
    response = requests.get(the_url,
        headers = {
            'Authorization':'Bearer '+ 'xxxxxxxxx',
            'Content-Type': 'application/json'
            }
        )
    #We use json to load our request response
    response_data = json.loads(response.text)
    #We loop through the result to navigate down to where our data i
    for i in response_data['data']:
    #We extract the access token here
        pageAccessToken = i['access_token']
    return pageAccessToken


def totalReaction(datelist):
    print(datelist)

