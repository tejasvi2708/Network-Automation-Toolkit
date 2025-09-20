import yaml
from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader

# Load device info
with open("inventory.yaml") as f:
    inventory = yaml.safe_load(f)

device = inventory['devices'][0]

# Create config from template
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("interface_config.j2")
config = template.render({
    "interface": "GigabitEthernet2",
    "description": "Configured by Netmiko",
    "ip": "192.0.2.20",
    "mask": "255.255.255.0"
})
config_lines = config.strip().splitlines()

# Connect and push
net_connect = ConnectHandler(
    device_type=device['platform'],
    host=device['host'],
    username=device['username'],
    password=device['password'],
    port=device['port']
)

output = net_connect.send_config_set(config_lines)

# Replace 'abhimanyu' with a custom name in logs (not on device)
custom_output = output.replace("abhimanyu", "Cisco_IOSXE")


print("Push Result:\n")

print(custom_output)

net_connect.disconnect()

