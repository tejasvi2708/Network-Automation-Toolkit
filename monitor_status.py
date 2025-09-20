import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()
import credentials

url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

username = credentials.username
password = credentials.password
auth = HTTPBasicAuth(username, password)

response = requests.get(url, headers=headers, auth=auth, verify=False)

if response.status_code == 200:
    data = response.json()
    print("Interface Status:")
    print(data)
else:
    print(f"Failed to retrieve interface: {response.status_code}")

