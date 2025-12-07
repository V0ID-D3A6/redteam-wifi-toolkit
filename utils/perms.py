import os
import sys

def require_root():
    if os.geteuid() != 0:
        print("[!] This tool must be run as root")
        sys.exit(1)

def require_write(path):
    if os.path.exists(path) and not os.access(path, os.W_OK):
        print(f"[!] No write permission to {path}")
        print("    Fix with: sudo chown -R $USER output/")
        sys.exit(1)
