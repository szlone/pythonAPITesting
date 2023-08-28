import jsonpath
import requests
import json


# API URL
url = "https://reqres.in/api/users/2"

# Read input Json File
jsonfile = open('E:\\MyCourses\\RestAPI\\pythonProject\\UpdateUser.json', 'r')
json_input = jsonfile.read()
request_json = json.loads(json_input)
print(request_json)

# Make PUT request with JSON input body
response = requests.put(url, request_json)
print(response.content)

# Validating Response Code
assert response.status_code == 200

# Fetch  Header from Response
print(response.headers.get('Content-Length'))

# Parse response to JSON format
response_json = json.loads(response.text)

# Pick Id JSON Path
Updated_li = jsonpath.jsonpath(response_json, 'UpdatedAt')
print(Updated_li[0])
