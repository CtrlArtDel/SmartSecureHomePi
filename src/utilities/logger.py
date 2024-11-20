import logging
import os

# Function to configure centralized logging
def configure_logger(log_file="logs/system.log", log_level=logging.INFO):
    # Create logs directory if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Configure logging
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),       # Log to file
            logging.StreamHandler()             # Log to console
        ]
    )
    return logging.getLogger("SmartSecure")

