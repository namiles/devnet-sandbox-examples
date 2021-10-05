#!/usr/bin/env python

from ncclient import manager
import xml.dom.minidom


# Always-On Sandbox Host
HOST = "sandbox-iosxe-latest-1.cisco.com"
# NETCONF Port
PORT = 830
# User Credentials
USER = "developer"
PASS = "C1sco12345"


def main():
    """
    Main method that retrieves the interfaces config via NETCONF.
    """
    with manager.connect(
        host=HOST,
        port=PORT,
        username=USER,
        password=PASS,
        hostkey_verify=False,
        device_params={"name": "default"},
        allow_agent=False,
        look_for_keys=False,
    ) as m:

        with open("interfaces_filter.xml", "r") as f:
            try:
                interfaces = m.get_config("running", f.read())
                print(xml.dom.minidom.parseString(interfaces.xml).toprettyxml())
            except Exception as e:
                print("Something went wrong.")
                print(e)

if __name__ == "__main__":
    main()
