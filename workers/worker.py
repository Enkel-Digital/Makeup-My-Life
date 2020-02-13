import requests
import os
from dotenv import load_dotenv
load_dotenv()

base_url = 'https://api.twitter.com/'
search_url = '{}1.1/search/tweets.json'.format(base_url)
access_token = os.getenv('BEARER_TOKEN') 

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)    
}

search_params = {
    'q': 'Makeup',
    'result_type': 'recent',
    'count': 2
}

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

if search_resp.status_code == 200 :
    tweet_data = search_resp.json()
    for tweet in tweet_data["statuses"] :
        print(tweet['entities'])
        # for t in tweet['entities']['user_mentions'] :
        #     print(t)
else :
    print('Result for' , search_url , 'is unsuccesful')