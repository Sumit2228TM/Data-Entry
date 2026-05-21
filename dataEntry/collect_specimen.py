'''
The given script is used to collect respective specimens -
'''

import requests
import json

BASE_URL   = "https://test.openspecimen.org/rest/ng"
LOGIN_NAME = ""
PASSWORD   = ""
DOMAIN     = "openspecimen"

session = requests.Session()
session.headers.update({"Content-Type": "application/json"})

auth_response = session.post(f"{BASE_URL}/sessions", json={ 
    "loginName": LOGIN_NAME,
    "password":  PASSWORD,
    "domain":    DOMAIN
})
    
auth = auth_response.json()
session.headers.update({"X-OS-API-TOKEN": auth["token"]})

if auth_response.status_code == 200:
    print("Auth Successful")
else:
    print("Unauth Access")
    exit()
    
collect = session.post(f"{BASE_URL}/specimens",json={
    "visitId":17410,
    "specimenClass":"Fluid",
    "type":"Whole Blood",
    "cpId":782,
    "availableQty":10,
    "initialQty":10, 
    "reqId":11279,
    "status":"Collected",
    "receivedEvent":{
        "user":{
            "id":601
        }
    }
})

if collect.status_code == 200:
    print("Successfully collected specimens")
else:
    print("Failed to collect specimens")
    print(f"Error Details:{collect.text}")
    exit()
    
'''
Output - 

Auth Successful
Successfully collected specimens

'''
