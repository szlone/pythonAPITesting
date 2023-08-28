import jsonpath
import requests
import json

def test_oauth_api():
    token_url = "https://thetestingworldapi.com//Token"
    data = {'grant_type':'password', 'username':'admin','password': ''}
    response = requests.get(token_url , data)
    token_value = jsonpath.jsonpath(response.json(),'access_token')
    auth = {'Authorization': 'Bearer'+token_value[0]}
    print(response)
    API_URL = "https://thetestingworldapi.com/api/stDetails/1104"
    response = requests.get(API_URL,headers=auth)
    # json_response = json.loads(response.text)
    print(response.text)