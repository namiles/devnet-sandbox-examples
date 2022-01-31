#!/usr/bin/env python

import requests
import json


# Always-On Sandbox Host
HOST = "sandbox-iosxe-latest-1.cisco.com"
# RESTCONF Port
PORT = 443
# User Credentials
USER = "developer"
PASS = "C1sco12345"


def main():
    url = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/"
    headers = {
        "Content-Type": "application/yang-data+json",
        "Accept": "application/yang-data+json",
    }
    payload = json.dumps(
        {
            "Cisco-IOS-XE-native:username": [
                {
                    "name": "restconfuser",
                    "privilege": 15,
                    "password": {"password": "rEStc0n4us3rpas$woRd!"},
                }
            ]
        }
    )

    response = requests.post(
        url, headers=headers, data=payload, verify=False, auth=(USER, PASS)
    )
    if response.ok:
        print(response.status_code)
        print("User created. Use the get_configured_users module to verify.")
    else:
        print(f"Failed with status code {response.status_code}")


if __name__ == "__main__":
    main()
