import sqlalchemy as db
import psycopg2
import os
import requests
from dotenv import load_dotenv
load_dotenv()

URL_ADDON = os.getenv('DATABASE_URL_ADDON')

def orm_config() :
    #ORM connection
    engine = db.create_engine('postgresql+psycopg2://{}'.format(URL_ADDON))
    connection = engine.connect()
    metadata = db.MetaData()
    tweets = db.Table('tweets', metadata , autoload=True , autoload_with=engine)


    return metadata, tweets, connection

def twitter_conn() :
    base_url = 'https://api.twitter.com/'
    search_url = '{}1.1/search/tweets.json'.format(base_url)
    access_token = os.getenv('BEARER_TOKEN') 

    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)    
    }

    search_params = {
        'q': 'Makeup',
        'result_type': 'recent',
        'count': 10
    }

    #Send request to Twitter API
    search_resp = requests.get(search_url, headers=search_headers, params=search_params)

    return search_resp

def data_get_and_insert(search_resp, metadata, tweets, connection) :

    id = None
    print(search_resp.status_code)
    if search_resp.status_code == 200 :

        #convert text into a data object (dictionary) for Python 
        tweet_data = search_resp.json()

        #Get data from Twitter API
        for tweet in tweet_data["statuses"] :
            text = tweet['text']
            time = tweet['created_at']
            name = tweet['user']['screen_name']
            print('FIRST DATA' , text +'\n'+ time +'\n'+ name + '\n')

            #ORM query 
            query = tweets.insert().values(name = name , text = text , time = time).returning(tweets.c.id)
            result = connection.execute(query)

    else :
        print('Request unsuccesful')

if __name__ == '__main__':
    orm_config()
    metadata, tweets, connection = orm_config()
    search_resp = twitter_conn()
    data_get_and_insert(search_resp, metadata, tweets, connection)