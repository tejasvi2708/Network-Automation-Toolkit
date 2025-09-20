import yaml
from jinja2 import Environment, FileSystemLoader

def load_data():
    return {
        "interface": "GigabitEthernet2",
        "description": "Configured by Automation",
        "ip": "192.0.2.10",
        "mask": "255.255.255.0"
    }

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('interface_config.j2')

config_data = load_data()
output = template.render(config_data)

print("Generated Config:\n")
print(output)

