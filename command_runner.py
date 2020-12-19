from scrapli.driver.core import IOSXEDriver
import variables
from datetime import datetime

# Set Constants
UNAME = variables.USERNAME
PWORD = variables.PASSWORD
DEVICES = variables.DEVICE_LIST
COMMANDS = variables.COMMANDS
OUTFILE = variables.OUTPUT_FILE

# Get the current date & time
now = datetime.now()
strnow = now.strftime("%d/%m/%Y %H:%M:%S")

# Craft the data to write to the output file
data = "\n" + strnow + "\n"

# Write the current date & time to the top of the output file
with open(OUTFILE, "w") as outfile:
    outfile.write(data)

# Create an empty list to store all the devices
devices = []

# Create a device counter
device_count = 0

# Read list of devices from device_list.txt
with open(DEVICES, "r") as infile:
    for line in infile:
        devices.append(line.strip())
        device_count += 1

# Create an empty list to store the commands
commands = []

# Read list of devices from device_list.txt
with open(COMMANDS, "r") as cmds_file:
    for line in cmds_file:
        commands.append(line.strip())

# Insert the command "show run | inc hostname" at the beginning of the list of commands
commands.insert(0, 'show run | inc hostname')

# Create a counter to display progress to user
counter = 1

# For each device loaded from the input file, populate a dictionary object with connection details
for ip_addr in devices:
    my_device = {
        "host": ip_addr,
        "auth_username": UNAME,
        "auth_password": PWORD,
        "auth_secondary": PWORD,
        "auth_strict_key": False,
        "transport": "paramiko"
    }

    # Create and open the connection object, send the list of commands and store the responses
    conn = IOSXEDriver(**my_device)
    conn.open()
    response = conn.send_commands(commands)
    
    # Extract the result of the first command - this should be the hostname
    hostname = response.data[0].result

    # Create a variable to store the heading (hostname & IP) formatted nicely
    data = "\n" + "=" * 85 + "\n" + hostname + ", Mngt IP: " + ip_addr + "\n" + "=" * 85 + "\n"

    # For each command loaded from commands.txt, loop through each command and add the command output to the data variable
    for command in response.data:
        # We don't want to do this for if the output contains 'hostname'
        if "hostname" not in command.result:
            # Append the command result
            data = data + command.result + "\n"

    # Open the output file and write the data for this device before looping around for the next device
    with open(OUTFILE, "a") as outfile:
        outfile.write(data)
        
    # Print progress to stdout
    print(f"{counter} of {device_count} done.")
    counter += 1

# Print the completion message
print(f"All done. Yay. Check file: {OUTFILE}")
