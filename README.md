# mac_changer

This Python script allows you to fetch, store, and temporarily change the MAC address of your network interface on macOS, Linux, and Windows. Once you close the program, the MAC address is reverted back to its original value.

## Features

- Fetches and stores the original MAC address.
- Generates a random MAC address.
- Changes the MAC address temporarily.
- Reverts the MAC address back to the original upon exiting the program.
- Cross-platform support for macOS, Linux, and Windows.

## Requirements

- Python 3.x
- Administrative/Root privileges: The script requires elevated permissions to change the MAC address.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/mac-address-changer.git
cd mac-address-changer
```

2. Install dependencies:
- This script uses the Python standard library, so no additional dependencies are required.


## Usage

1. Run the script:
- macOS/Linux:
```bash
sudo python3 mac_changer.py
```

- Windows:
Run the script as an administrator:
```bash
python mac_changer.py
```
2. Follow the instructions:
- The script will display your current MAC address and generate a new random one.
- Press 'Enter' when you're ready to revert the MAC address back to its original value.

## Important Notes

- Network Interface: The script uses en0 as the default interface for macOS, and Ethernet for Windows. You may need to adjust this depending on your system's configuration.
- Compatibility: The script should work on most versions of macOS, Linux, and Windows. However, different network setups might require customization.
- Legal Disclaimer: Changing your MAC address can affect your network connectivity and might be illegal in some jurisdictions. Ensure that you have the proper authorization before using this script.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
