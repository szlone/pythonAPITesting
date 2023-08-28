import jsonpath
import requests
import json

# adding all the tables at once....
def test_add_new_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open('E:/MyCourses/RestAPI/pythonProject/StudentMS/CreateNewStudent.json', 'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL, json_request)
    id = jsonpath.jsonpath(response.json(), 'id')
    # print(response.text)
    print(id[0])

    tech_api_url = "https://thetestingworldapi.comapi/technicalskills"
    f = open('E:/MyCourses/RestAPI/pythonProject/StudentMS/technicalDetails.json', 'r')
    json_request = json.loads(f.read())
    json_request['id'] = int(id[0])
    json_request['st_id'] = id[0]
    response = requests.post(tech_api_url, json_request)
    print(response.text)
    # id = jsonpath.jsonpath(response.json(), 'id')

    address_api_url = "https://thetestingworldapi.comapi/addresses"
    f = open('E:/MyCourses/RestAPI/pythonProject/StudentMS/Address.json', 'r')
    json_request = json.loads(f.read())
    json_request['st_id'] = id[0]
    response = requests.post(address_api_url, json_request)
    print(response.text)
    # id = jsonpath.jsonpath(response.json(), 'id')

    final_details_api_url = "https://thetestingworldapi.comapi/FinalStudentDetails/"+str(id[0])
    f = open('E:/MyCourses/RestAPI/pythonProject/StudentMS/Address.json', 'r')
    json_request = json.loads(f.read())
    response = requests.post(address_api_url, json_request)
    print(response.text)
