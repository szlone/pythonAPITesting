import jsonpath
import requests
import json


# API URL
url = "https://reqres.in/api/users"

# Read input Json File
jsonfile = open('E:\\MyCourses\\RestAPI\\pythonProject\\PytestExamples\\CreateUser.json', 'r')
json_input = jsonfile.read()
request_json = json.loads(json_input)
print(request_json)

# Make POST request with JSON input body
response = requests.post(url, request_json)
print(response.content)

# Validating Response Code
assert response.status_code == 201

# Fetch  Header from Response
print(response.headers.get('Content-Length'))

# Parse response to JSON format
response_json = json.loads(response.text)

# Pick Id JSON Path
idx = jsonpath.jsonpath(response_json, 'Id')
#print(idx[0])
print(jsonpath.jsonpath(response_json, 'Id'))



