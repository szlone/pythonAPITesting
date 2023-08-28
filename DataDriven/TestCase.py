import jsonpath
import requests
import json
import openpyxl
from DataDriven import Library
# the path for DataDriven is not known, hence have to create __init_.py in that folder


# adding all the tables at once....
def test_add_multiple_students():
    # API details
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open('E:/MyCourses/RestAPI/pythonProject/StudentMS/StudentData.xlsx', 'r')
    json_request = json.loads(f.read())

    obj = Library.Common("E:/MyCourses/RestAPI/pythonProject/StudentMS/StudentData.xlsx", "Sheet1")
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()

    # Excel Code
    wk = openpyxl.load_workbook('E:/MyCourses/RestAPI/pythonProject/StudentMS/StudentData.xlsx')
    sh = wk['sheet1']
    rows = sh.max_row
    for i in range(2, rows+1):  # note first row is the header plus have to add 1 to include the last row
        updated_json_request = obj.update_request_with_data(i,json_request, keyList)
        response = requests.post(api_url, updated_json_request)
        print(response)
