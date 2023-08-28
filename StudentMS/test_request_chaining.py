import jsonpath
import requests
import json


# adding all the tables at once....
def test_add_new_data():
    global id
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open('E:/MyCourses/RestAPI/pythonProject/StudentMS/CreateNewStudent.json', 'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL, json_request)
    id = jsonpath.jsonpath(response.json(), 'id')
    # print(response.text)
    print(id[0])


def test_get_data():
    # using the id we get from above and using it here... is known as request chaining
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.get(API_URL)
    # json_response = json.loads(response.text)
    print(response.text)
