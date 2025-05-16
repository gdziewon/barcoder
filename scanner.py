from evdev import InputDevice, InputEvent, categorize, ecodes
import threading
import queue
from typing import Generator, Optional
from config import BARCODE_END_KEY, GLYPH_NOT_FOUND, keymap

class Scanner:
    def __init__(self, device_path: str):
        self.device: InputDevice = InputDevice(device_path)
        self.barcodes: queue.Queue[str] = queue.Queue()
        self._stop_event: threading.Event = threading.Event()
        self._thread: Optional[threading.Thread] = None

    def __enter__(self) -> "Scanner":
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.stop()

    def start(self) -> None:
        """Start listening for barcodes"""
        if self._thread and self._thread.is_alive():
            return
        
        try:
            self.device.grab()
        except IOError as e:
            raise RuntimeError(f"Failed to grab device: {str(e)}")
        
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._read_loop)
        self._thread.start()

    def stop(self) -> None:
        """Stop listening and clean up resources"""
        if self._thread and self._thread.is_alive():
            self._stop_event.set()
            self._thread.join(timeout=1)
            
        try:
            self.device.ungrab()
        except IOError:
            pass  # Already ungrabbed
        
        self.device.close()

    def _read_loop(self) -> None:
        """Internal event processing loop"""
        barcode = []
        try:
            for event in self.device.read_loop():
                if self._stop_event.is_set():
                    break
                
                if event.type == ecodes.EV_KEY:
                    self._process_key_event(event, barcode)
        finally:
            self.barcodes.put(None)  # Sentinel for shutdown

    def _process_key_event(self, event: InputEvent, barcode: list) -> None:
        """Handle individual key press events"""
        data = categorize(event)

        if data.keystate == 1: # Key press
            if data.scancode == BARCODE_END_KEY:
                self.barcodes.put(''.join(barcode))
                barcode.clear()
            else:
                char = keymap.get(data.scancode, GLYPH_NOT_FOUND)
                barcode.append(char)

    def read(self) -> Generator[str, None, None]:
        """Generate barcodes as they are scanned"""
        while True:
            try:
                barcode = self.barcodes.get() # Blocking call
                if barcode is None:
                    return
                yield barcode
            except queue.Empty:
                if not self._thread.is_alive():
                    return
