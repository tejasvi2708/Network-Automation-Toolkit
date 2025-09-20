import requests
from requests.auth import HTTPBasicAuth
import urllib3
import credentials
from datetime import datetime

urllib3.disable_warnings()

url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

username = credentials.username
password = credentials.password
auth = HTTPBasicAuth(username, password)

response = requests.get(url, headers=headers, auth=auth, verify=False)

# Simple datetime string: YYYYMMDD_HHMMSS
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file_path = f"interface_status_{timestamp}.txt"

if response.status_code == 200:
    data = response.json()
    print("Interface Status:")
    print(data)

    # Save JSON response as string to log file
    with open(log_file_path, "w") as log_file:
        log_file.write(str(data))

    print(f" Status saved to: {log_file_path}")

else:
    print(f"Failed to retrieve interface: {response.status_code}")
    with open(log_file_path, "w") as log_file:
        log_file.write(f"Failed to retrieve interface: {response.status_code}")

    print(f" Error logged to: {log_file_path}")
