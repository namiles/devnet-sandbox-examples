import requests
import json

# DevNet NX-OS Always on Sandbox
url = "https://sandbox-nxos-1.cisco.com:443/ins"
uname = "admin"
pw = "Admin_1234!"

payload = json.dumps({
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show ip int brief",
    "output_format": "json"
  }
})

headers = {
  'Content-Type': 'application/json',
}

response = requests.post(url, auth=(uname,pw), headers=headers, data=payload, verify=False).json()
print(json.dumps(response, indent=2, sort_keys=True))
