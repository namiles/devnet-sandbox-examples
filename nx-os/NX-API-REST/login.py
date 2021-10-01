import requests
import json

def get_token():
    """
    Returns token for interacting with NX-API REST.
    """

    # DevNet NX-OS always on Sandbox
    url = "https://sandbox-nxos-1.cisco.com/api/aaaLogin.json"
    payload = json.dumps({
        "aaaUser": {
            "attributes": {
                "name": "admin",
                "pwd": "Admin_1234!"
            }
        }
    }) 
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.post(url, headers=headers, data=payload, verify=False).json()
    token = response["imdata"][0]["aaaLogin"]["attributes"]["token"]

    return token
