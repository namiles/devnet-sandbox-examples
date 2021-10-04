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
    url = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/username"
    headers = {
        "Content-Type": "application/yang-data+json",
        "Accept": "application/yang-data+json",
    }

    response = requests.get(
        url, headers=headers, verify=False, auth=(USER, PASS)
    ).json()
    print(json.dumps(response, indent=2))


if __name__ == "__main__":
    main()
