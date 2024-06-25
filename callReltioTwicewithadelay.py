import requests
import time
import urllib.parse

def get_auth_token():
    auth_token = "s.AAAAoii1L_0gog0EAFKIGx5gNdYY8PBa1G4rrFiw4cPQqBueLGlGpfsaYAiC5QKTIaoFrAw5lgs0xZRuIHDFF9filpaUxbX0FlwpNmOlwxmeaiy-A6wnyeD9WWegwnuzzjmj3TnaE-sICQtHIJ34yOJJqBzeoXXJPE0kvMOjBQAy9PXCASI1-JdZ4Gs-AQ.irAhwEfPDQwT6SxX_085hk_KGgOTUyy5Ly3AB7mhbNoXcu4MEOiwQLhyUv1sa7Lj072UsNbz_ZmHJiqrgZROSQedQmYq9aMNKdsOloMwwot4y2P1sYay43ZCoXPri4VZvbCSvO7Z39Wj128al2mhhd4TAjaZbT9Gu-GBcDGKjV6uf8kzVfMk1IEP02IR_28i_dDl9pm6ojW3GH0ugNPU1p9A85uEcigXT6IOB4tX7b-Mosyo22w7Z5A4F9juAD6dEkI3icevqA2ILcjt_mRA3nfAL9YmcZj6EQn_tfPYAXo9WRRZevooX3DKzRAOeiF1qwSHP9k1x6M2LbWGwDUWCQ"
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
    endpoint1 = "https://gus-training.reltio.com/reltio/api/193YOmXw2aubJFm/entities/_conditional"
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
    endpoint2 = "https://gus-training.reltio.com/reltio/api/193YOmXw2aubJFm/entities/_search"
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
