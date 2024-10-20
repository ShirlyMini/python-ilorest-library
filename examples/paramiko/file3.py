bond_name = "bond0"  # Name of the bond interface
slaves = ["eth0", "eth1"]  # List of slave interfaces
bond_config = f"""
	DEVICE={bond_name}
    TYPE=Bond
    BONDING_OPTS="mode={mode} miimon=100"
    BOOTPROTO=none
    ONBOOT=yes
    """
commands1 = [ "sudo modprobe bonding",
 f'echo "{bond_config.strip()}" | sudo tee /etc/sysconfig/network-scripts/ifcfg-{bond_name}']

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host,  username=username, password=password)
for i in commands1:
    stdin,stdout, stderr = client.exec_command(i)
    output = (stdout.read().decode('utf-8'))
    print(output)
client.close()