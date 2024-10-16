## Creates a new Log file every 100 KB

import logging
from logging.handlers import RotatingFileHandler

# Create a rotating handler with max 100KB per file, keeping the last 5 files
handler = RotatingFileHandler('app.log', maxBytes=100*1024, backupCount=5)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

for i in range(1000):
    logger.info(f"Log entry {i}")
