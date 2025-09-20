# Network Automation Toolkit

A lightweight and modular Python toolkit designed for automating Cisco network devices. This project demonstrates how real-world network automation is performed using APIs, SSH-based configuration, and templating, ideal for network engineers starting with Python.

# What This Project Demonstrates

 - Automating configuration deployment using Netmiko

 - Monitoring device interfaces via RESTCONF
    Fetches the interface status from the device using RESTCONF.
    Prints the status output to the terminal.
    Creates a *timestamped .txt* file in the project directory containing the interface status (or error message).

 - Generating device configs using Jinja2 templates

 - Organizing device data with YAML-based inventory files

 - Secure and modular project structure for easy scaling


# Tools & Frameworks Used

 - Python	- Core scripting language
 - Netmiko - SSH-based config automation
 - Jinja2	- Templating for config generation
 - RESTCONF -	API-based interface monitoring
 - YAML	- Inventory and device data storage
 - Cisco DevNet Sandbox -	Testing lab for real devices
   
# Prerequisites

 - Python 3.8+
 - Git
 - Virtual environment (recommended)

# Setup Instructions
1. Clone the repository
git clone https://github.com/your-username/network-automation-toolkit.git
cd network-automation-toolkit

2. Set up virtual environment
python -m venv myenv
myenv\Scripts\activate  # For Windows

3. Install dependencies
pip install -r requirements.txt

# Credentials & Inventory Setup
 - inventory.yaml (NOT uploaded to GitHub)
 - credentials.py (NOT uploaded to Github)

This file contains device IPs, usernames, and passwords.
Do not upload this file to GitHub. It's ignored using .gitignore.
Use your own credentials in **inventory_example.yaml.**
Create a new file **credentials.py** which stores your own username and password


# How to Run the Scripts

 1. Generate Config (Jinja2)
python generate_config.py

 2. Push Config to Device (Netmiko)
python push_config.py

 3. Monitor Interface via RESTCONF
python monitor_status.py

## Final Notes

Built using Cisco's DevNet Sandbox — no real devices required

Secure by design — credentials are isolated from source code

Great starting point for job portfolios or real-world automation labs
