import ipaddress

ip = '192.168.0.1/24'


rede = ipaddress.ip_address(ip)

for ip in rede:
	print(rede)