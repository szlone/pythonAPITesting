import jsonpath
import requests
from requests.auth import HTTPBasicAuth
import json


def test_with_authentication():
    response = requests.get('https://api.github.com/', auth=HTTPBasicAuth('szlone','GitHub_TaakWine3873957'))
    print(response.text)
