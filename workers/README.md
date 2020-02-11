# Worker

## Installation
Ensure that pip and python is installed

`````
install pipenv for dependencies management
pip install --user pipenv
make sure the path is added to the system
`````
install Requests library for HTTP request
pipenv install requests
list of dependencies will be listed on Pipfile


## Authentication for Twitter
Create an account folloed by an app
https://developer.twitter.com/en/account/get-started
`````
Get your application tokens at "Keys and Access Tokens"
consumer key, consumer secret key, access token, access token secret 
`````
Use get_bearer_token.py to get Bearer Token 
Bearer Token is required to use the Request lib for Twitter API
`````

`````
## Fetch Data from API 
Insert the Bearer Token into worker.py
`````

Insert params for the Twitter API
Info about the endpoint of Twitter API 
https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets#
When the response status is 200, JSON formatted data will be returned 
