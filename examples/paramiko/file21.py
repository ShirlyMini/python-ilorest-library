import paramiko

# Define 3PAR array details
array_ip = 'your_array_ip'
username = 'your_username'
password = 'your_password'

# Establish SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(array_ip, username=username, password=password)

# Execute commands
def execute_command(command):
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')
    if error:
        print(f"Error: {error}")
    return output

# Get system info
system_info = execute_command('showsys')
print(system_info)

# Get volume list
volume_list = execute_command('showvol')
print(volume_list)

# Create a new volume
volume_name = 'new_volume'
volume_size = '100GB'
create_volume = execute_command(f'createvol {volume_name} {volume_size}')
print(create_volume)

# Close SSH connection
ssh.close()
