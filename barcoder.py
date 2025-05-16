#!/usr/bin/env python3
from scanner import Scanner
import sys

def barcoder(device_path: str) -> None:
    with Scanner(device_path) as scanner:
        for barcode in scanner.read():
            print(f"Scanned: {barcode}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: barcoder.py <device_path>")
        sys.exit(1)
    
    device_path = sys.argv[1]
    barcoder(device_path)