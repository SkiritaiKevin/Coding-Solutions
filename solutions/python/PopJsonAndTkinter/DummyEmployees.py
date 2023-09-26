import os 
import json
import requests

os.chdir(os.path.dirname(os.path.realpath(__file__)))

url = "http://www1.lasalle.edu/~blum/c341wks/dummy_employees.json"

myHeaders={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

myParams = {}

response = requests.get(url, params=myParams, headers=myHeaders)

employeeInfo = json.loads(response.text)

for employee in employeeInfo["data"]:
    employee.pop("employee_age")
    employee.pop("profile_image")

with open("newJson.json", "w") as newFile:
    newFile.write(json.dumps(employeeInfo, indent=2))


