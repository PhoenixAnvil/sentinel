import logging

# Create base logger
logger = logging.getLogger("sentinel")
logger.setLevel(logging.INFO)

# File handler (default)
file_handler = logging.FileHandler("sentinel.log")
file_handler.setLevel(logging.INFO)
file_format = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s"
)
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)

# Console handler (prints to stdout)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter("Sentinel: %(message)s")
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)
