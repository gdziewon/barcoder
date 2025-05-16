#!/usr/bin/env python3
from scanner import Scanner
from barcode_handler import BarcodeHandler
import sys

def barcoder(device_path: str) -> None:
    handler = BarcodeHandler()
    with Scanner(device_path) as scanner:
        for barcode in scanner.read():
            print(f"Scanned: {barcode}")
            res = handler.handle_barcode(barcode)
            if res:
                print(f"Handled barcode: {barcode}")
            else:
                print(f"No action for barcode: {barcode}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: barcoder.py <device_path>")
        sys.exit(1)
    
    device_path = sys.argv[1]
    barcoder(device_path)