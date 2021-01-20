import os



def WireguardConf(configs_path, private_key, ip_address, public_key=None, psk=None, dns=None, endpoint=None, allowed_ips=None, keep_alive = None):
    """Wireguard Configuration File Settings.
	Args:
		configs_path (str):
			Required. Path to wireguard configuration files. E.g. '/home/user/wireguard-configs'.
		private_key (str):
			Required. Private key that will be used to decrypt vpn traffic. E.g. '6NtN9j0Qm3rXMC0Mb6nPoFZS6lTkyqQAGHQD2k3klFY='.
		ip_address (str):
			Required. IP address of wireguard server. E.g. "10.120.0.45".
		public_key (str):
			Optional. Public key that will be used to encrypt vpn traffic. E.g. '6NtN9j0Qm3rXMC0Mb6nPoFZS6lTkyqQAGHQD2k3klFY='.
		psk (str):
			Optional. Pre-Shared Key. Default: None
		dns (str):
			Optional. DNS Server IP address. E.g. "8.8.8.8".
        endpoint (str):
			Optional. Endpoint of VPN traffic. Default: None.
        allowed_ips (str):
			Optional. Range of allowed IP addresses in CIDR format. E.g "0.0.0.0/0". Default: None.
        keep_alive (str):
			Optional. Time in secs to keep connection active. Default: None.
	"""

    for filename in os.listdir(configs_path):
        if filename.endswith(".conf"):
            with open (os.path.join(configs_path, filename), "r+") as file_input:
                with open (os.path.join(configs_path, str('modified_' + filename)), "w") as output:
                    for line in file_input:
                        if 'PrivateKey' in line:
                            output.write(str('PrivateKey = ' + private_key))
                            output.write("\n")
                        elif 'PublicKey' in line and public_key != None:
                            output.write(str('PublicKey = ' + public_key))
                            output.write("\n")
                        elif 'Address' in line:
                            output.write(str('Address = ' + ip_address))
                            output.write("\n")
                        elif 'PresharedKey' in line and psk != None:
                            output.write(str('PresharedKey = ' + psk))
                            output.write("\n")
                        elif 'PresharedKey' in line and psk == None:
                            continue # skip writing psk line if we don't have one.
                        elif 'DNS' in line and dns != None:
                            output.write(str('DNS = ' + dns))
                            output.write("\n")
                        elif 'Endpoint' in line and endpoint != None:
                            output.write(str('Endpoint = ' + endpoint))
                            output.write("\n")
                        elif 'AllowedIPs' in line and allowed_ips != None:
                            output.write(str('AllowedIPs = ' + allowed_ips))
                            output.write("\n")
                        elif 'PersistentKeepalive' in line and keep_alive != None:
                            output.write(str('PersistentKeepalive = ' + keep_alive))
                            output.write("\n")
                        else:
                            output.write(line)
        else:
            continue
