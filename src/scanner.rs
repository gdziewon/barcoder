use evdev::{Device, EventSummary, KeyCode};
use std::collections::HashMap;

pub struct Scanner {
    device: Device,
}

pub struct Barcode {
    pub code: String,
}

pub struct BarcodeFetcher<'a> {
    scanner: &'a mut Scanner
}

impl<'a> Iterator for BarcodeFetcher<'a> {
    type Item = Barcode;

    fn next(&mut self) -> Option<Self::Item> {
        self.scanner.read()
    }
}

impl<'a> Scanner {
    pub fn fetch_barcodes(&'a mut self) -> BarcodeFetcher<'a> {
        BarcodeFetcher { scanner: self }
    }
}

impl Scanner {
    pub fn new(device_path: &str) -> Self {
        let mut device = Device::open(device_path).expect("Failed to open device");
        device.grab().expect("Failed to grab device");
        Scanner { device }
    }

    pub fn read(&mut self) -> Option<Barcode> {
        let scancode_map = HashMap::from([
            (2, '1'),
            (3, '2'),
            (4, '3'),
            (5, '4'),
            (6, '5'),
            (7, '6'),
            (8, '7'),
            (9, '8'),
            (10, '9'),
            (11, '0'),
            (28, '\n'),
        ]);

        let mut code: String = String::new();
        loop {
            for event in self.device.fetch_events().unwrap() {
                match event.destructure() {
                    EventSummary::Key(_, KeyCode::KEY_ENTER, 1) => {
                        return Some(Barcode { code: code });
                    }
                    EventSummary::Key(_, key_type, 1) => {
                        if let Some(&c) = scancode_map.get(&key_type.code()) {
                            code.push(c);
                        }
                    }
                    _ => {}
                }
            }
        }
    }
}

