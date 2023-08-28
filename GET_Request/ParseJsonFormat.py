import jsonpath
import requests
import json

# API URL
url = "https://regres.in/api/users?page2"

# send get request -74
response = requests.get(url)

# Parse response to Json format
json_response =  json.loads(response.text)
print(json_response)

# Fetch value using json-path
pages = jsonpath.jsonpath(json_response,'total_page') # this will produce a list of values
print(pages(0)) # the '0' inside the brackets represents the index value
assert pages[0] == 4 # number value we should expect, therefore no error if true - any other number entered will give error

# Fetch value using advance json-path
for i in range(0, 3):
    first_name = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
    print((first_name[0]))
