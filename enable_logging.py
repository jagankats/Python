import logging
import os
from datetime import datetime

class ColorFormatter(logging.Formatter):
    def format(self, record):
        # ANSI escape codes for colors
        LOG_COLORS = {
            'DEBUG': '\033[94m',  # Blue
            'INFO': '\033[37m',  # Green
            'WARNING': '\033[93m',  # Yellow
            'ERROR': '\033[91m',  # Red
            'CRITICAL': '\033[1;91m',  # Bold Red
            'RESET': '\033[0m'  # Reset
        }
        color = LOG_COLORS.get(record.levelname, LOG_COLORS['RESET'])
        message = super().format(record)
        return f"{color}{message}{LOG_COLORS['RESET']}"


def enable_logging(log_file_path: str, level: int = logging.INFO) -> str:
    log_dir = os.path.dirname(log_file_path)
    base_name = os.path.basename(log_file_path)
    name, ext = os.path.splitext(base_name)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    new_log_filename = f"{name}_{timestamp}{ext}"
    new_log_path = os.path.join(log_dir, new_log_filename)

    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(level)

    # Remove existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # File handler (no color)
    file_handler = logging.FileHandler(new_log_path)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'))

    # Console handler (with color)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(ColorFormatter(
        '%(asctime)s - %(levelname)s - %(message)s'))

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info("Logging initialized.")
    return new_log_path


if __name__ == "__main__":
    log_path = enable_logging("logs/script.log")
    print(f"Logging to file: {log_path}")

    logging.debug("Debug message")
    logging.info("Info message")
    logging.warning("Warning message")
    logging.error("Error message")
    logging.critical("Critical message")
