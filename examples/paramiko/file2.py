username = "your_username"
password = "your_password"
host = "192.168.1.100"
commands1 = [ "nmcli connection show",
 f"nmcli con modify {eth_p1} ipv4.method manual ipv4.addresses {host_ip1}/24",
 f"nmcli con down {eth_p1}",
 f"nmcli con up  {eth_p1}",
f"nmcli con modify {eth_p2} ipv4.method manual ipv4.addresses {host_ip2}/24",
f"nmcli con down {eth_p2}",
f"nmcli con up  {eth_p2}"]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host,  username=username, password=password)
for i in commands1:
    stdin,stdout, stderr = client.exec_command(i)
    output = (stdout.read().decode('utf-8'))
    print(output)
client.close()