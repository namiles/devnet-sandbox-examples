import requests
import json
from login import get_token

url = "https://sandbox-nxos-1.cisco.com:443/api/mo/sys/intf/lb-[lo513].json"
token = get_token()
cookies = {}
cookies['APIC-cookie'] = token
headers = {
  'Content-Type': 'application/json',
  'Accept':'application/json'
}

response = requests.get(url, headers=headers, cookies=cookies, verify=False).json()
print(json.dumps(response, indent=2, sort_keys=True))
