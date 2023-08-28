import requests

# API URL
url = "https://regres.in/api/users?page2"

# send get request -74
response = requests.get(url)
print(response)


# Display Response Content -74
print(response.content)
print(response.headers)

# Validate Status Code -75
print( response.status_code)

# Validate Response Content-75
assert response.status_code == 200

# Fetch Response Header -76
print( response.headers)
print( response.headers.get('Date'))
print( response.headers.get('Server'))

# Fetch Cookies -76
print( response.cookies)

# Fetch Encoding -76
print( response.encoding)

# Fetch Elapsed Time (i.e sending request and get response) -76
print( response.elapsed)

