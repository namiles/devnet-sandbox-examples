from ncclient import manager
import sys

# DevNet NX-OS Always on sandbox
HOST = 'sandbox-nxos-1.cisco.com'
# use the NETCONF port for your IOS-XE device
PORT = 830
# use the user credentials for your IOS-XE device
USER = 'admin'
PASS = 'Admin_1234!'

def get_capabilties():
    # Connects using the NETCONF protocol
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         look_for_keys=False, allow_agent=False) as m:

        # print all NETCONF capabilities
        for capability in m.server_capabilities:
            print(capability.split('?')[0])

def main():
    get_capabilties()

if __name__ == '__main__':
    sys.exit(main())