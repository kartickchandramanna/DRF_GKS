import requests
import json

URL = "http://127.0.0.1:8000/stu_create/"


data = {
    'name':'Clery Clinton',
    'roll':804,
    'city':'Manhattan'
}


json_data = json.dumps(data)   # this convert python data type to json format

print(json_data)

r = requests.post(url=URL , data=json_data)  # here we are sending json data to the backend 

data = r.json()

print(data)
