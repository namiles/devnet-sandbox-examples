#!/usr/bin/env python

import requests


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

    response = requests.delete(url, headers=headers, auth=(USER, PASS), verify=False)
    if response.ok:
        print(response.status_code)
        print(
            "Loopback deleted. Use the get_loopback or get_interfaces_config module to verify."
        )
    else:
        print(f"Failed with status code {response.status_code}")


if __name__ == "__main__":
    main()
