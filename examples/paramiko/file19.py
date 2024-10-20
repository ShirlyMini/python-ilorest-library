import paramiko
 
# Define the SSH credentials
ssh_username = "your_username"
ssh_password = "your_password"
ssh_ip_address = "192.168.1.100"
 
# Command to check the firewall status
command = "sudo ufw status"
 
# Establish an SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ssh_ip_address, username=ssh_username, password=ssh_password)
 
# Execute the command
stdin, stdout, stderr = ssh.exec_command(command)
 
# Provide sudo password if required
stdin.write(ssh_password + '\n')
stdin.flush()
 
# Print the output and errors
print(stdout.read().decode())
print(stderr.read().decode())
 
# Close the SSH connection
ssh.close()
has context menu