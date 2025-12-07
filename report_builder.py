#!/usr/bin/env python3

import argparse
from utils.helpers import load_json
from utils.logger import setup_logger

log = setup_logger()

def main():
    try:
        lan = load_json("output/lan_map.json")
        wifi = load_json("output/wifi_scan.json")
    except FileNotFoundError as e:
        log.error(e)
        log.error("Run network_mapper.py and wifi_recon.py first")
        return

parser.add_argument(
    "-o", "--output",
    default="output/report.md",
    help="Output report file"
)

    report = f"""

# Red Team Recon Report

## LAN
Hosts discovered: {lan['host_count']}

## Wi‑Fi
Networks discovered: {wifi['network_count']}
"""

    with open("output/report.md", "w") as f:
        f.write(report)

    log.info("Report written to output/report.md")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user")
    except Exception as e:
        print(f"[!] Error: {e}")
