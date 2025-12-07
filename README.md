# 🛡️ Red Team Wi-Fi Toolkit

**Red Team Wi-Fi Toolkit** is a lightweight offensive security toolkit designed for **Wi-Fi and LAN reconnaissance**, written in Python.  
The project focuses on **clean code**, professional CLI design, logging, and structure commonly used in **red team / penetration testing tools**.

> ⚠️ **For educational purposes and authorized security testing only.**

---

## ✨ Features

- 📡 **Wi‑Fi Recon**
  - Passive Wi‑Fi scanning
  - JSON result export
- 🌐 **LAN Network Mapper**
  - Local network host discovery
  - Structured network mapping
- 📝 **Report Builder**
  - Unified report generation (Markdown)
- 🧰 **Shared Infrastructure**
  - Professional logging system
  - Root permission enforcement
  - CLI powered by `argparse`
  - Modular project architecture

---

## 📁 Project Structure

```text
redteam-wifi-toolkit/
├── network_mapper.py      # LAN network mapping
├── wifi_recon.py          # Wi-Fi reconnaissance
├── report_builder.py      # Report generator
├── requirements.txt
├── README.md
├── output/
│   ├── lan_map.json
│   └── wifi_scan.json
└── utils/
    ├── logger.py          # Centralized logging
    ├── perms.py           # Permission checks
    ├── helpers.py
    └── __init__.py


# 🛡️ Red Team Wi-Fi Toolkit

**Red Team Wi-Fi Toolkit** is a lightweight offensive security toolkit designed for **Wi-Fi and LAN reconnaissance**, written in Python.  
The project focuses on **clean code**, professional CLI design, logging, and structure commonly used in **red team / penetration testing tools**.

> ⚠️ **For educational purposes and authorized security testing only.**

---

## ✨ Features

- 📡 **Wi‑Fi Recon**
  - Passive Wi‑Fi scanning
  - JSON result export
- 🌐 **LAN Network Mapper**
  - Local network host discovery
  - Structured network mapping
- 📝 **Report Builder**
  - Unified report generation (Markdown)
- 🧰 **Shared Infrastructure**
  - Professional logging system
  - Root permission enforcement
  - CLI powered by `argparse`
  - Modular project architecture

---
ℹ️ Help Menu

Each tool provides a built‑in help menu:

python3 wifi_recon.py -h
python3 network_mapper.py -h
python3 report_builder.py -h

---

⚙️ Requirements

Python 3.9+

Linux (Kali / Parrot / Ubuntu recommended)

Root privileges (for network operations)

Install dependencies:

pip3 install -r requirements.txt


---

📡 Wi‑Fi Recon
sudo python3 wifi_recon.py -i wlan0 -o output/wifi_scan.json


Arguments

-i, --interface — Wireless interface

-o, --output — Output JSON file

---

🌐 Network Mapper (LAN)
sudo python3 network_mapper.py -i eth0 -o output/lan_map.json


Arguments

-i, --interface — Network interface

-o, --output — Output JSON file

---

📝 Report Builder
python3 report_builder.py -o output/report.md


Generates a consolidated report based on:

- output/lan_map.json

- output/wifi_scan.json

---

👤 Author

Created by V0IDD3A6
Red Team / Offensive Security Enthusiast
