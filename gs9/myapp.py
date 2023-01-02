import requests
import json

URL = 'http://127.0.0.1:8000/studentapi/'

# def get_data(id = None):
#     data = {}
#     if id is not None:
#         data = {'id':id}
#     json_data = json.dumps(data)

#     r = requests.get(url=URL , data=json_data)
#     print(r.text)
#     data = r.json() # It convert json data to python dict.

#     print(data)

# get_data()

def post_data():
    data = {
        'name':'Krishna',
        'roll':101,
        'city':'Mothura',
    }
    headers = {'content-type' : 'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url=URL , data=json_data, headers=headers)
    data = r.json()
    print(data)

post_data()
