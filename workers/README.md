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


