import requests
import time
import urllib.parse

def get_auth_token():
    auth_token = "Auth token here"
    return auth_token

def send_api_call(endpoint, method, headers, params=None, data=None):
    if params:
        endpoint = f"{endpoint}?{urllib.parse.urlencode(params)}"

    if method == "GET":
        response = requests.get(endpoint, headers=headers)
    elif method == "POST":
        response = requests.post(endpoint, headers=headers, json=data)
    elif method == "PUT":
        response = requests.put(endpoint, headers=headers, json=data)
    elif method == "DELETE":
        response = requests.delete(endpoint, headers=headers, json=data)
    else:
        raise ValueError("Invalid HTTP method specified")
    
    return response.url, response.json()

def main():
    auth_token = get_auth_token()
    
    # API call to endpoint1 with POST method
    endpoint1 = "https://env.reltio.com/reltio/api/{{tenantId}}/entities/_conditional"
    params1 = {
        "filter": "(equals(type,'configuration/entityTypes/Individual') and equals(attributes.FirstName,'Donny') and equals(attributes.LastName,'Doe') and equals(attributes.Email.Email,'donnydoe@email.com'))",
        "options": "partialOverride",
        "applyIfNoMatches": "true",
        "returnMatches": "true"
    }
    method1 = "POST"
    headers1 = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    data1 = [
        {
            "type": "configuration/entityTypes/Individual",
            "attributes": {
                "FirstName": [
                    {
                        "type": "configuration/entityTypes/Individual/attributes/FirstName",
                        "value": "Donny"
                    }
                ],
                "LastName": [
                    {
                        "type": "configuration/entityTypes/Individual/attributes/LastName",
                        "value": "Doe"
                    }
                ],
                "Email": [
                    {
                        "value": {
                            "Email": [
                                {
                                    "type": "configuration/entityTypes/Individual/attributes/Email/attributes/Email",
                                    "value": "donnydoe@email.com"
                                }
                            ]
                        }
                    }
                ],
                "Address": [
                    {
                        "value": {
                            "AddressLine1": [
                                {
                                    "value": "addressline 1"
                                }
                            ],
                            "City": [
                                {
                                    "value": "Houston"
                                }
                            ],
                            "StateProvince": [
                                {
                                    "value": "TX"
                                }
                            ],
                            "Country": [
                                {
                                    "value": "USA"
                                }
                            ],
                            "Zip": [
                                {
                                    "value": {
                                        "Zip5": [
                                            {
                                                "value": "1234"
                                            }
                                        ],
                                        "Zip4": [
                                            {
                                                "value": "456"
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            },
            "crosswalks": [
                {
                    "type": "configuration/sources/ThirdPartyList",
                    "value": "89239001",
                    "sourceTable": "customer"
                }
            ]
        }
    ]
    url1, response1 = send_api_call(endpoint1, method1, headers1, params=params1, data=data1)
    print("Constructed URL 1:", url1)
    print("Response 1:", response1)

    # Add a 20-second delay
    time.sleep(300)

    # API call to endpoint2 with GET method
    endpoint2 = "https://env.reltio.com/reltio/api/{{tenantId}]/entities/_search"
    params2 = {
        "filter": "(equals(type,'configuration/entityTypes/Individual') and (equals(attributes.PartyKey,'{{party_key}}')))",
        "select": "uri,type,attributes.PartyKey,attributes.FirstName,attributes.LastName,attributes.Email.Email,attributes.Phone.Number,attributes.Address,crosswalks"
    }
    method2 = "GET"
    headers2 = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    url2, response2 = send_api_call(endpoint2, method2, headers2, params=params2)
    print("Constructed URL 2:", url2)
    print("Response 2:", response2)

if __name__ == "__main__":
    main()
