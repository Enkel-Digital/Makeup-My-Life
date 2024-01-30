# Worker

## Installation

Ensure that pip and python is installed

install pipenv for dependencies management. List of dependencies will be listed on Pipfile. Make sure the pipenv path is added to the system.
```sh
pip install --user pipenv
```

install Requests library for HTTP request
```sh
pipenv install requests
```

install psycopg2 for library to access PostgreSQL Database
```sh
pipenv install psycopg2
```

install python-dotenv to add environment variables into the app 
```sh
pipenv install python-dotenv
```

install SQLAlchemy for ORM database
```sh
pipenv install SQLAlchemy
```

## Authentication for Twitter
Create an account followed by application creation  on Twitter Developer Account. More information can be found in https://developer.twitter.com/en/account/get-started
Get your application tokens at "Keys and Access Tokens"
- consumer key
- consumer secret key 
- access token
- access token secret 

Bearer Token can be generated from get_bearer_token.py  
Bearer Token is required to use the Request lib for Twitter API

## Fetch Data from API 
- Insert the Bearer Token into worker.py
- Insert params for the Twitter API
Info about the endpoint of Twitter API https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets#

## Environment variables set up
- Create a .env file and input the variables 
- Call dotenv library and os to get the desired variables 
variables description :
1.  BEARER_TOKEN
    Token that consist of all kinds of character.
    OAuth 2.0 generated from Account Token and Account Token Secret from Twitter developer page, Once these two tokens are available, use get_bearer_token.py to generate Bearer Token for the account
2.  ACC_TOKEN 
    Token that consist of all kinds of character.
    This token can be generated after user create an account and a new aplication in the developer page.
3.  ACC_TOKEN_SECRET
    Token that consist of all kinds of character.
    This token can be generated after user create an account and a new aplication in the developer page.
4.  USERNAME
    consist of string/int that the user created in PostgreSQL
5.  PASSWORD
    consist of string/int that the user created in PostgreSQL
6.  DB_NAME
    consist of string/int that the user created in PostgreSQL
7.  DB_PORT and DB_HOST
    default value in PostgreSQL are DB_PORT = 5432 , DB_HOST = localhost
8.  DATABASE_URL_ADDON 
    an URL for ORM endpoint of PostgreSQL that consist of 
    USERNAME:PASSWORD@HOST:PORT/DATABASE_NAME

## Connect to PostgreSQL server and queries
- start postgres server with psql -U <user> <database_name>
- insert all the params to psycopg2.connect 
- use INSERT query to insert data each time it is fetched
- commit and close connection and its cursor

## ORM with SQLAlchemy setup and usage
SQLAlchemy is an Object-Relation Mapper that interact with database with Python programming language 
- set up the engine and connection with the URL (with params to Postgres)
- keep all database information into Metadata object 
- query with Python languange. More info can be found here https://docs.sqlalchemy.org/en/13/core/tutorial.html#connecting


