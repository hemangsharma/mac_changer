import os
import uuid
import platform
import subprocess

def get_mac_address():
    # Fetch the current MAC address
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                    for elements in range(0,2*6,2)][::-1])
    return mac

def set_mac_address(new_mac):
    os_type = platform.system()
    interface = 'en0'  # Default interface for macOS, might be different on other OS
    
    if os_type == "Darwin":  # macOS
        subprocess.run(["sudo", "ifconfig", interface, "ether", new_mac])
    elif os_type == "Linux":
        subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    elif os_type == "Windows":
        interface = "Ethernet"  # Replace with your Windows network adapter name
        subprocess.run(f'netsh interface set interface "{interface}" disabled', shell=True)
        subprocess.run(f'netsh interface set interface "{interface}" enabled', shell=True)
    else:
        raise Exception("Unsupported OS")

def revert_mac_address(original_mac):
    set_mac_address(original_mac)

def generate_random_mac():
    import random
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

def main():
    original_mac = get_mac_address()
    print(f"Original MAC: {original_mac}")

    # Store the original MAC address
    with open('original_mac.txt', 'w') as f:
        f.write(original_mac)

    # Generate and set a new MAC address
    new_mac = generate_random_mac()
    print(f"New MAC: {new_mac}")
    set_mac_address(new_mac)

    input("Press Enter to revert MAC address and exit...")

    # Revert to the original MAC address
    revert_mac_address(original_mac)
    print(f"Reverted to Original MAC: {original_mac}")

if __name__ == "__main__":
    main()
