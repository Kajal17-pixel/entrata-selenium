from loguru import logger
import os

# Create logs directory if it doesn't exist
if not os.path.exists("reports/logs"):
    os.makedirs("reports/logs")

# Add logger with file output
logger.add("reports/logs/test_log.log", format="{time} {level} {message}", level="INFO")
