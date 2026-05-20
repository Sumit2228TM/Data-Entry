'''
The given script is used to create a cp registration -
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

cpr = session.post(f"{BASE_URL}/collection-protocol-registrations/", json={
    "cpShortTitle":"TCPAPI1",
    "ppid":"TCPAPI_001",
    "registrationDate": "2026-05-19",
    "participant" :{
        "firstName" : "Patrick",
        "lastName":"Patil",
        "emailAddress":"patrick05@gmail.com",
        "gender": "Male",
        "birthDate":"2005-03-14",
        "vitalStatus":"Alive",
        "races":["Asian"]
    },
    "dataEntryStatus":"COMPLETE"
})

if cpr.status_code == 200:
    print("CPR Successfull")
else:
    print("CPR Unsuccessfull")
    print(f"Error details: {cpr.text}")
    exit()
    
''' 
the script returns the following output  - 

Auth Successful
CPR Successfull

'''    
    
