print("\n=====================================")
print("        COMMAND RUNNER SETUP         ")
print("=====================================")

print("\nvariables.txt .....Created")
with open("variables.py", "w") as vars_file:
	vars_file.write('USERNAME = "<ENTER_USERNAME_HERE>"\nPASSWORD = "<ENTER_PASSWORD_HERE"\nDEVICE_LIST = "device_list.txt"\nCOMMANDS = "commands.txt"\nOUTPUT_FILE = "output.txt"')

print("commands.txt ......Created")
with open("commands.txt", "w") as cmds_file:
	cmds_file.write('show ip int brief')

print("device_list.txt ...Created")
with open("device_list.txt", "w") as device_file:
	device_file.write('1.1.1.1\n2.2.2.2\n3.3.3.3')

print("\nPlease create a Python Virtual Environment and install the required libraries:\n\n   - python3 -m venv .\n   - pip install -r requirements.txt\n\n")
