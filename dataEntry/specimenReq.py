'''
The given script is used to create specimen requirements for primary, derived and aliquots -
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

requirements = session.post(f"{BASE_URL}/specimen-requirements",json={ 
    "type":"Whole Blood",
    "cpShortTitle":"TCPAPI1",
    "anatomicSite":"Not Specified",
    "laterality":"Not Specified",
    "pathology":"Not Specified",
    "initialQty":10,
    "collectionProcedure":"Not Specified",
    "collectionContainer":"EDTA Vacutainer",
    "specimenClass":"Fluid",
    "storageType":"Auto",   
    "eventLabel":"Baseline"
})

if requirements.status_code == 200:
     print("Specimen Requirement added")
else:
    print("Failed to add Specimen Requirement")
    print(f"Error Details:{requirements.text}")
    exit()



derived = session.post(f"{BASE_URL}/specimen-requirements/11270/derived",json={
    "type": "Plasma",
    "anatomicSite": "Not Specified",
    "laterality": "Not Specified",
    "pathology": "Not Specified",
    "quantity":5,
    "specimenClass":"Fluid",
    "storageType":"Auto"
})

if derived.status_code == 200:
    print("Derived Specimen created")
else:
    print("Failed to create derived specimen")
    print(f"Error Details:{derived.text}")
    exit()



aliquot = session.post(f"{BASE_URL}/specimen-requirements/11279/aliquots",json={
    "noOfAliquots":5,
    "qtyPerAliquot":1,
    "storageType":"Auto"
})

if aliquot.status_code == 200:
    print("Aliquot Created")
else:
    print("Failed to create aliquot")
    print(f"Error Details:{aliquot.text}")
    exit()
    

'''
the script returns the following output  - 

Auth Successful
Specimen Requirement added
Derived Specimen created
Aliquot Created

'''  