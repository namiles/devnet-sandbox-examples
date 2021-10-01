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
    "input": "show vlan brief",
    "output_format": "json"
  }
})

headers = {
  'Content-Type': 'application/json',
}

response = requests.post(url, auth=(uname,pw), headers=headers, data=payload, verify=False)
data = response.json()
print(json.dumps(data, indent=2, sort_keys=True))
print()
print(response.status_code == requests.codes.ok)
print(response.status_code)
print(requests.codes.ok)

