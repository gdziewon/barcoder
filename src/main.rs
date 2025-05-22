use std::path::Path;

mod scanner;
mod dispatcher;

fn main() {
    let mut scanner = scanner::Scanner::new("/dev/barcoder");
    let config_path = Path::new("/home/gdziewon/Documents/rust/barcoder/barcoder.yaml");
    let dispatcher = dispatcher::Dispatcher::new(config_path);
    for barcode in scanner.fetch_barcodes() {
        println!("Scanned barcode: {}", barcode.code);
        dispatcher.dispatch(&barcode);
    }
}
