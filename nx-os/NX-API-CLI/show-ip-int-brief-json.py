import sys
import json
import requests

# DevNet NX-OS Always on Sandbox
HOST = "sandbox-nxos-1.cisco.com"
# Port
PORT = 443
# DevNet Supplied Username
USER = "admin"
# DevNet Supplied Password
PASS = "Admin_1234!"


def main():
    payload = json.dumps(
        {
            "ins_api": {
                "version": "1.0",
                "type": "cli_show",
                "chunk": "0",
                "sid": "sid",
                "input": "show ip int brief",
                "output_format": "json",
            }
        }
    )

    headers = {
        "Content-Type": "application/json",
    }

    response = requests.post(
        f"https://{HOST}:{PORT}/ins",
        auth=(USER, PASS),
        headers=headers,
        data=payload,
        verify=False,
    )
    if response.ok:
        data = response.json()
        print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == "__main__":
    sys.exit(main())
