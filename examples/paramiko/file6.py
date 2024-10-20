import paramiko
 
# Define the SSH credentials
ssh_username = "your_username"
ssh_password = "your_password"
ssh_ip_address = "192.168.1.100"
 
# Define the local file and remote path
local_file_path = "/path/to/local/file.txt"
remote_file_path = "/home/your_username/file.txt"
 
# Establish an SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ssh_ip_address, username=ssh_username, password=ssh_password)
 
# Create an SFTP session
sftp = ssh.open_sftp()
sftp.put(local_file_path, remote_file_path)
sftp.close()
 
# Close the SSH connection
ssh.close()
 
print(f"Uploaded {local_file_path} to {remote_file_path} on {ssh_ip_address}.")