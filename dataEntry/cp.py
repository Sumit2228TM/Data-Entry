'''
The given script is used to create a cp -
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
    
cp = session.post(f"{BASE_URL}/collection-protocols",json={
    "title":"Test CP API1",
    "shortTitle":"TCPAPI1",
    "principalInvestigator":{
        "loginName":LOGIN_NAME,
        "domain": DOMAIN
    },
    "activityStatus":"Active",
    "cpSites":[
        {
            "siteName":"Sumit Site A",
            "code":"SSA"
        },
        {
            "siteName":"Sumit Site B",
            "code":"SSB"
            
        }
        ],
})

if cp.status_code == 200:
    print("CP Created")
else:
    print("Failed to create CP")
    print(f"Error details: {cp.text}")
    exit()


''' 
the script returns the following output  - 

Auth Successful
CP Created

'''
