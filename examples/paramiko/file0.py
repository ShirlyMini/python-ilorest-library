username = "your_username"
password = "your_password"
host = "192.168.1.100"
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host,  username=username, password=password)
stdin, stdout, stderr = client.exec_command("date;multipath -ll")
output = (stdout.read().decode('utf-8'))
print(output)
client.close()