import requests
import json
from login import get_token

url = "http://sbx-nxos-mgmt.cisco.com/api/mo/sys.json"
token = get_token()
cookies = {}
cookies['APIC-cookie'] = token
headers = {
  'Content-Type': 'application/json',
  'Accept':'application/json'
}

response = requests.get(url, headers=headers, cookies=cookies, verify=False).json()["imdata"][0]["topSystem"]["attributes"]
print(json.dumps(response, indent=2, sort_keys=True))
print()
print("HOSTNAME:", response["name"])
print("SERIAL NUMBER:", response["serial"])
print("UPTIME:", response["systemUpTime"])
print("CURRENT STATE:", response["status"])
