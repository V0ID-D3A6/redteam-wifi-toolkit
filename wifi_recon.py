#!/usr/bin/env python3

import argparse
from datetime import datetime
from utils.perms import require_root
from utils.helpers import save_json
from utils.logger import setup_logger
log = setup_logger()

from utils.banner import show

log = setup_logger()

def main():
    require_root()

    args = parse_args()

    log.info(f"Using interface: {args.interface}")
    log.info(f"Saving results to: {args.output}")

    
def parse_args():
    parser = argparse.ArgumentParser(
        description="Wi-Fi reconnaissance tool (passive scan)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-i", "--interface",
        required=True,
        help="Wireless interface (e.g. wlan0)"
    )

    parser.add_argument(
        "-o", "--output",
        default="output/wifi_scan.json",
        help="Output file path"
    )

    return parser.parse_args()


    print("Running with root privileges")

if __name__ == "__main__":
    try:
        main()
    except PermissionError as e:
        print(f"[!] {e}")
    except KeyboardInterrupt:
        print("\n[!] User terminated")

    parser = argparse.ArgumentParser(description="Wi-Fi Recon Tool")
    parser.add_argument("-i", "--interface", required=True)
    parser.add_argument("-o", "--output", default="output/wifi_scan.json")
    args = parser.parse_args()

    log.info(f"Scanning Wi-Fi on interface {args.interface}")

    networks = [
        {"ssid": "TestNet", "bssid": "AA:BB:CC:DD:EE:FF", "encryption": "WPA2"},
        {"ssid": "<hidden>", "bssid": "11:22:33:44:55:66", "encryption": "Open"}
    ]

    data = {
        "timestamp": datetime.now().isoformat(),
        "interface": args.interface,
        "network_count": len(networks),
        "networks": networks
    }

    save_json(args.output, data)
    log.info(f"Saved Wi-Fi scan to {args.output}")

if __name__ == "__main__":
    try:
        main()
    except PermissionError as e:
        log.error(e)
    except KeyboardInterrupt:
        log.warning("User terminated")

log.info("Starting Wi-Fi recon")
log.warning("Monitor mode not detected")
log.error("No scan results found")
