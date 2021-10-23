# FrootVPN Wireguard .conf File Editor


## Overview

A simple function for batch editing multiple wireguard .conf files.

## Use-Case
When you create a new Wireguard Public key on the FrootVPN website, the .conf files need to be manually modified to include the Private Key, address of FrootVPN Wireguard server and the Pre-Shared Key (if applicable). If you choose to download all 45+ wireguard configuation files this is a hassle.




```python

from batch_editor import WireguardConf

WireguardConf(<path to folder containing .conf files>, <private key>, <ip_address>)

```

## Arguments

```
	Args:
		configs_path (str):
			Required. Path to wireguard configuration files. 
		private_key (str):
			Required. Private key that will be used to decrypt vpn traffic.
		ip_address (str):
			Required. IP address of wireguard server. 
		public_key (str):
			Optional. Public key that will be used to encrypt vpn traffic.
		psk (str):
			Optional. Pre-Shared Key. Default: None
		dns (str):
			Optional. DNS Server IP address.
        endpoint (str):
			Optional. Endpoint of VPN traffic. Default: None.
        allowed_ips (str):
			Optional. Range of allowed IP addresses in CIDR format.
        keep_alive (str):
			Optional. Time in secs to keep connection active. Default: None.
```

## Expected Behaviour
Outputs the modified .conf files within same directory and with preface 'modified' within file name.
