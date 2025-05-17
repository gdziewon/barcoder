#!/usr/bin/env python3
from scanner import Scanner
from handler import BarcodeHandler
from logs import setup_logging
import logging

def barcoder(device_path: str = "/dev/barcoder") -> None:
    setup_logging()
    handler = BarcodeHandler()
    with Scanner(device_path) as scanner:
        for barcode in scanner.read():
            logging.info(f"Scanned barcode: {barcode}")
            res = handler.handle_barcode(barcode)
            if res:
                logging.info(f"Action executed for barcode: {barcode}")
            else:
                logging.warning(f"No action found for barcode: {barcode}")


if __name__ == "__main__":
    barcoder()