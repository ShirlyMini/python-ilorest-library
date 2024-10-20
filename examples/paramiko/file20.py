import paramiko

# Define Brocade switch details
switch_ip = 'your_switch_ip'
username = 'your_username'
password = 'your_password'

# Establish SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(switch_ip, username=username, password=password)

# Execute commands
def execute_command(command):
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')
    if error:
        print(f"Error: {error}")
    return output

# Get switch info
switch_info = execute_command('switchShow')
print(switch_info)

# Get port info
port_info = execute_command('portShow')
print(port_info)

# Get fabric info
fabric_info = execute_command('fabricShow')
print(fabric_info)

# Configure a new zone
zone_name = 'new_zone'
zone_members = '10:00:00:00:00:00:00:01,20:00:00:00:00:00:00:02'
configure_zone = execute_command(f'zoneCreate {zone_name} {zone_members}')
print(configure_zone)

# Enable the zone configuration
enable_zone = execute_command('zoneEnable')
print(enable_zone)

# Save configuration
save_config = execute_command('configSave')
print(save_config)

# Close SSH connection
ssh.close()