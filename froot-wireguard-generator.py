import os
import subprocess
import configparser
import pycountry
import flag


if not os.path.exists("/usr/local/bin/wg-quick"):
    print("DEPENDENCY ERROR: wg-quick is not installed. Run `brew install wireguard-tools` to install")
    exit(1)

# script variables
froot_confs_dir_name = "froot-wireguard-configs"
froot_confs_dir_path = os.path.join(
    os.path.dirname(__file__), froot_confs_dir_name)
output_dir = "/usr/local/etc/wireguard"

# wg conf variables
wg_dns = "1.1.1.1"
wg_presharedkey = subprocess.getoutput('wg genpsk')
wg_allowedips = "0.0.0.0/0"
wg_persistentkeepalive = "15"
wg_privkey = subprocess.getoutput('wg genkey')
wg_pubkey = subprocess.getoutput(f'echo {wg_privkey} | wg pubkey')

print(f"Add pub key to FrootVPN: {wg_pubkey}")
print(f"Add psk key to FrootVPN: {wg_presharedkey}")
wg_address = input("Allowed IP: ")

# iterate over confs
for config_file in os.listdir(froot_confs_dir_path):
    if config_file.endswith(".conf"):
        config_file_path = os.path.join(froot_confs_dir_path, config_file)
        # alpha2 refers to 2 digit country codes. See: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
        config_file_alpha2 = config_file[:2].upper()
        country = pycountry.countries.get(alpha_2=config_file_alpha2)
        country_flag = flag.flag(config_file_alpha2)
        config = configparser.ConfigParser()
        config.read(config_file_path)
        config.set(section="Interface", option="privatekey", value=wg_privkey)
        config.set(section="Interface", option="dns", value=wg_dns)
        config.set(section="Interface", option="address", value=wg_address)
        config.set(section="Peer", option="allowedips", value=wg_allowedips)
        config.set(section="Peer", option="persistentkeepalive",
                   value=wg_persistentkeepalive)
        config.set(section="Peer", option="presharedkey",
                   value=wg_presharedkey)
        with open(os.path.join(output_dir, config_file), 'w', encoding="utf8") as configfile:
            config.write(configfile)
