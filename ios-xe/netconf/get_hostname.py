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


def main():
    """
    Main method that retrieves the hostname from config via NETCONF.
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

        hostname_filter = """
                          <filter>
                              <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                                  <hostname></hostname>
                              </native>
                          </filter>
                          """
        result = m.get_config("running", hostname_filter)
        xml_doc = xml.dom.minidom.parseString(result.xml)
        hostname = xml_doc.getElementsByTagName("hostname")
        print(hostname[0].firstChild.nodeValue)


if __name__ == "__main__":
    sys.exit(main())
