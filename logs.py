import logging
from systemd import journal

def setup_logging(log_path: str = "barcoder.log"):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Log to journald
    journald_handler = journal.JournaldLogHandler()
    journald_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
    logger.addHandler(journald_handler)

    # Log to file
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
    logger.addHandler(file_handler)
