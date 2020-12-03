from scrapli.driver.core import IOSXEDriver

my_device = {
    "host": "ios-xe-mgmt.cisco.com",
    "auth_username": "developer",
    "auth_password": "C1sco12345",
    "port": 8181,
    "auth_strict_key": False,
}

conn = IOSXEDriver(**my_device)
conn.open()
response = conn.send_command("show ip int b")
print(response.result)

#response = conn.send_configs(['interface loop5678', 'desc Matt Test', 'ip add 5.6.7.8 255.255.255.0'])
#response = conn.send_commands(["show ip int b", "show run int lo5678"])
#print(response.result)
