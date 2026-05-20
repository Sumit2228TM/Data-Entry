'''
The given script is used to create a cp event-
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

events = session.post(f"{BASE_URL}/collection-protocol-events",json={
    "eventLabel":"Baseline",
    "clinicalDiagnosis":"3-part fracture of surgical neck of humerus",
    "clinicalStatus":"Operative",
    "activityStatus":"Active",
    "defaultSite":"Sumit Site A",
    "collectionProtocol":"Test CP API1"
})

if events.status_code == 200:
    print("Event Created")
else:
    print("Event Creation unsuccessfull")
    print(f"Error Details:{events.text}")
    exit()
    
''' 
the script returns the following output  - 

Auth Successful
Event Created

'''  