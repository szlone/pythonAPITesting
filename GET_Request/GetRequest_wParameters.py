import requests

Params = {'name': 'testingworld', 'email': 'testingworld@gmail.com', 'number': '+1-345-878654'}
response = requests.get('https://httpbin.org/get', params=Params)
print(response.text)
