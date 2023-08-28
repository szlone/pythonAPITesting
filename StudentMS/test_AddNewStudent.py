import jsonpath
import requests
import json


def test_add_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open('E:/MyCourses/RestAPI/pythonProject/StudentMS/CreateNewStudent.json', 'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL, json_request)
    print(response.text)

def test_get_student_data():
    # get student with id=7767874 details...
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/7767874,"
    response = requests.post(API_URL)
    json_response = json.loads(response.text)
    # below commented outis the second approach...
    # json_response = response.json()
    id = jsonpath.jsonpath(json_response, 'data.id')
    assert id == 7767874

def test_update_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/7767874,"
    f = open('E:/MyCourses/RestAPI/pythonProject/StudentMS/UpdateStudent.json', 'r')
    json_request = json.loads(f.read())
    response = requests.put(API_URL, json_request)
    print(response.text)


def test_delete_student_data():
    # get student with id=7767874 details...
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/7767874,"
    response = requests.delete(API_URL)
    json_response = json.loads(response.text)
    print(response.text)
    #id = jsonpath.jsonpath(json_response, 'data.id')
    #assert id == 7767874