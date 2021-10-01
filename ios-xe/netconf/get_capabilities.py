#!/usr/bin/env python

from ncclient import manager
import sys


# Always-On Sandbox Host
HOST = "sandbox-iosxe-latest-1.cisco.com"
# NETCONF Port
PORT = 830
# User Credentials
USER = "developer"
PASS = "C1sco12345"


def main():
    """
    Main method that prints netconf capabilities of remote device.
    """
    with manager.connect(
        host=HOST,
        port=PORT,
        username=USER,
        password=PASS,
        hostkey_verify=False,
        device_params={"name": "default"},
        look_for_keys=False,
        allow_agent=False,
    ) as m:

        # print all NETCONF capabilities
        print("***Here are the Remote Devices Capabilities***")
        for capability in m.server_capabilities:
            print(capability.split("?")[0])


if __name__ == "__main__":
    sys.exit(main())
