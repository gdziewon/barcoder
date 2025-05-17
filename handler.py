from pydantic import BaseModel, ValidationError
from typing import Dict, List, Optional
import yaml
import os
import subprocess
from pathlib import Path

class ActionConfig(BaseModel):
    description: str
    command: str
    args: List[str] = []
    env: Dict[str, str] = {}

class BarcoderConfig(BaseModel):
    version: str
    default: Optional[ActionConfig] = None
    mappings: Dict[str, ActionConfig]

class BarcodeHandler:
    def __init__(self, config_path: str = "barcoder.yaml"):
        self.config_path = Path(config_path)
        self.config = self._load_and_validate_config()

    def _load_and_validate_config(self) -> BarcoderConfig:
        try:
            with open(self.config_path, 'r') as f:
                raw_config = yaml.safe_load(f)
            return BarcoderConfig.model_validate(raw_config)
        
        except ValidationError as e:
            self._handle_validation_error(e)

        except Exception as e:
            raise RuntimeError(f"Config loading failed: {str(e)}") from e

    def _handle_validation_error(self, error: ValidationError):
        errors = []
        for err in error.errors():
            loc = ".".join(map(str, err['loc']))
            msg = err['msg']
            errors.append(f"Config error at {loc}: {msg}")
        raise ValueError("\n".join(errors))

    def handle_barcode(self, barcode: str) -> bool:
        if action := self.config.mappings.get(barcode):
            return self._execute_action(action)
        elif self.config.default:
            return self._execute_action(self.config.default)
        return False

    def _execute_action(self, action: ActionConfig) -> bool:
        env = os.environ.copy()
        env.update(action.env)
        
        try:
            result = subprocess.run(
                [action.command] + action.args,
                env=env,
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error executing {action.description}: {e.stderr}")
            return False