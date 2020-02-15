import psycopg2
import requests
import os
import worker
from dotenv import load_dotenv
load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

class DatabaseConnection:
    def __init__(self) :
        try :
            #connect to postgres server
            self.connection = psycopg2.connect(database =  DB_NAME  , user =  USERNAME , password = PASSWORD  , host = DB_HOST  , port = DB_PORT )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print('CONNECTED!')
        except :
            print('connection unsuccessful')

    def twitter_conn(self) :
        base_url = 'https://api.twitter.com/'
        search_url = '{}1.1/search/tweets.json'.format(base_url)
        access_token = os.getenv('BEARER_TOKEN') 

        search_headers = {
            'Authorization': 'Bearer {}'.format(access_token)    
        }

        search_params = {
            'q': 'Makeup',
            'result_type': 'recent',
            'count': 3
        }

        #Send request to Twitter API
        search_resp = requests.get(search_url, headers=search_headers, params=search_params)

        return search_resp

    def data_get_and_insert(self, search_resp) :

        #Postgres query and params
        sql_query = """INSERT INTO tweets(name, text, time) VALUES ( %s, %s, %s) RETURNING id ;"""
        id = None

        if search_resp.status_code == 200 :

            #convert text into a data object (dictionary) for Python 
            tweet_data = search_resp.json()

            #Get data from Twitter API
            for tweet in tweet_data["statuses"] :
                text = tweet['text']
                time = tweet['created_at']
                name = tweet['user']['screen_name']
                print('FIRST DATA' , text +'\n'+ time +'\n'+ name )

                #Insert data into postgres
                self.cursor.execute(sql_query , (name, text, time))
                id = self.cursor.fetchone()[0] 
                print('SECOND DATA' , text +'\n'+ time +'\n'+ name )
            
            #Postgres commit and close cursor and connection
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
        else :
            print('Result for' , search_url , 'is unsuccesful')

if __name__ == '__main__' :
    db = DatabaseCon()
    db.twitter_conn()
    search_resp = db.twitter_conn()
    db.data_get_and_insert(search_resp)