import RPi.GPIO as GPIO
import time
from utilities.logger import configure_logger

# Configure logger
logger = configure_logger()

# Handles PIR sensor input and triggers subsequent actions.
class MotionDetector:
    def __init__(self, pin=4, motion_timeout=300):
        self.pin = pin
        self.motion_timeout = motion_timeout
        self.last_motion_time = None
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
        logger.info("MotionDetector initialized with pin: %d and timeout: %d seconds", self.pin, self.motion_timeout)

    def detect_motion(self):
        """
        Detect motion by reading the PIR sensor input.
        If motion is detected, record the time and return True.
        """
        if GPIO.input(self.pin):
            self.last_motion_time = time.time()
            logger.info("Motion detected at pin %d", self.pin)
            return True
        return False

    def is_idle(self):
        """
        Check if the system is idle by comparing the last motion time with the timeout.
        """
        if self.last_motion_time is None:
            logger.debug("No motion detected yet.")
            return True
        idle = time.time() - self.last_motion_time > self.motion_timeout
        if idle:
            logger.debug("System is idle. No motion for more than %d seconds.", self.motion_timeout)
        return idle

    def cleanup(self):
        """
        Cleanup GPIO settings when done.
        """
        GPIO.cleanup()
        logger.info("GPIO cleanup completed.")

