from scrapli.driver.core import IOSXEDriver
import variables

conn = IOSXEDriver(**variables.my_device)
conn.open()
response = conn.send_command('show ip int brief | inc Vlan')
print(response.result)

#response = conn.send_configs(['interface loop5678', 'desc Matt Test', 'ip add 5.6.7.8 255.255.255.0'])
#response = conn.send_commands(["show ip int b", "show run int lo5678"])
#print(response.result)
