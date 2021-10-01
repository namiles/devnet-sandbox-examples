#!/usr/bin/env python

from ncclient import manager
import sys
import xml.dom.minidom


# Always-On Sandbox Host
HOST = "sandbox-iosxe-latest-1.cisco.com"
# NETCONF Port
PORT = 830
# User Credentials
USER = "developer"
PASS = "C1sco12345"

# XML file to open
FILE = "interfaces.xml"


def get_configured_interfaces(xml_filter):
    """
    Main method that retrieves the interfaces from config via NETCONF.
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
        with open(xml_filter) as f:
            return m.get_config("running", f.read())


def main():
    interfaces = get_configured_interfaces(FILE)
    print(xml.dom.minidom.parseString(interfaces.xml).toprettyxml())


if __name__ == "__main__":
    sys.exit(main())
