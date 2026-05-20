'''
The given script is used to create a visit and collect respective specimens -
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
    
visits = session.post(f"{BASE_URL}/visits/collect", json={ 
    "visit": {
        "eventLabel": "Baseline",   
        "clinicalDiagnoses": [
            "3-part fracture of surgical neck of humerus" 
        ],
        "activityStatus":"Active",  
        "eventId":904,
        "site":"Sumit Site A",
        "cpTitle":"TCPAPI1",
        "cprId":7993,
        "status":"Complete"
    },
    "specimens":[
        {
            "specimenClass":"Fluid",
            "type":"Whole Blood",
            "cpId":782,
            "availableQty":"10",
            "initialQty":"10", 
            "reqId":11279,
            "status":"Collected",
            "receivedEvent":{
                "user":{
                    "id":601
                }
            }
        }
    ]
}) 

if visits.status_code == 200:
    print("Success")
else:
    print("Failed")
    print(f"Error Details: {visits.text}")
    exit()
    
'''
Output - 

Auth Successful
Specimen Collected successfully

'''
