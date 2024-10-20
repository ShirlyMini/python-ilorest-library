import paramiko

# Define the SSH credentials
username = "your_username"
password = "your_password"
host = "192.168.1.100"

# Define the NIC interface name
nic_interface = "eth0"

# Define the log file path and name on the remote system
log_file_path = "/var/log/tcpdump"
log_file_name = f"tcpdump_{nic_interface}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# Establish an SSH connection to the remote system
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=username, password=password)

# Run the tcpdump command on the remote system
tcpdump_cmd = f"tcpdump -i {nic_interface} -vv -s 0 -W 1000 -G 3600 -w {log_file_path}/{log_file_name}"
stdin, stdout, stderr = ssh.exec_command(tcpdump_cmd)

# Print the output and errors
print(stdout.read().decode())
print(stderr.read().decode())

# Close the SSH connection
ssh.close()