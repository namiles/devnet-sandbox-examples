#!/usr/bin/env python

import requests
import json
import sys


# Always-On Sandbox Host
HOST = "sandbox-iosxe-latest-1.cisco.com"
# RESTCONF Port
PORT = 443
# User Credentials
USER = "developer"
PASS = "C1sco12345"


def main():
    url = f"https://{HOST}:{PORT}/restconf/data/ietf-interfaces:interfaces/interface=Loopback800"
    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json",
    }

    response = requests.get(url, headers=headers, auth=(USER, PASS), verify=False)
    if response.ok:
        print(json.dumps(response.json(), indent=2))


if __name__ == "__main__":
    sys.exit(main())
