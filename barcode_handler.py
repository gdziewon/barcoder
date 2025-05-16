import yaml
import subprocess
import os

class BarcodeHandler:
    def __init__(self, config_path="./barcoder.yaml"): # FIXME: just for testing
        self.config = self._load_config(config_path)
        self._validate_config()

    def _load_config(self, path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    def _validate_config(self):
        required_keys = ['description', 'command']
        for barcode, action in self.config['mappings'].items():
            if not all(key in action for key in required_keys):
                raise ValueError(f"Invalid config for barcode {barcode}")

    def handle_barcode(self, barcode):
        action = self.config['mappings'].get(barcode)
        if not action:
            return False
        
        env = os.environ.copy()
        env.update(action.get('env', {}))
        
        try:
            subprocess.run(
                [action['command']] + action.get('args', []),
                env=env,
                check=True,
                text=True,
                capture_output=True
            )
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error executing {action['description']}: {e.stderr}")
            return False
