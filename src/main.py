import os
import cv2
import threading
import logging
from datetime import datetime
from sensors.motion_detection import MotionDetector
from sensors.sensor_manager import SensorManager
from ai.face_recognition_module import FaceRecognition
from ai.fall_detection import FallDetection
from storage.video_recorder import VideoRecorder
from storage.encryption_manager import EncryptionManager
from storage.cloud_integration import CloudIntegration
from audio.audio_communication import TwoWayAudio
from audio.voice_control import VoiceControl
from notifications.notifications import Notifier
from notifications.telegram_notifier import TelegramNotifier
from system.energy_manager import EnergyManager
from utilities.logger import configure_logger
import yaml

# Configure centralized logger
logger = configure_logger(log_file="data/logs/system.log", log_level=logging.INFO)

# Load configuration and secrets
def load_yaml(file_path):
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return {}
    except yaml.YAMLError as e:
        logger.error(f"Error reading YAML file {file_path}: {e}")
        return {}

config = load_yaml("config/config.yaml")
secrets = load_yaml("config/secrets.yaml")

# Merge configuration with secrets
def merge_config_with_secrets(config, secrets):
    for key, value in config.items():
        if isinstance(value, dict):
            config[key] = merge_config_with_secrets(value, secrets)
        elif isinstance(value, str) and value.startswith("!secret"):
            secret_key = value.split("!secret ")[1]
            config[key] = secrets.get(secret_key, f"Missing secret: {secret_key}")
    return config

config = merge_config_with_secrets(config, secrets)

# Validate configuration
required_keys = ["motion_detection", "face_recognition", "video", "notifications"]
for key in required_keys:
    if key not in config:
        logger.critical(f"Missing required configuration key: {key}")
        exit(1)

def encrypt_and_upload(video_path, config, encryption_manager, cloud_integration):
    try:
        encryption_manager.encrypt_file(video_path)
        logger.info("Video encrypted successfully.")
    except Exception as e:
        logger.error(f"Error encrypting video: {e}")
        return

    try:
        if config["cloud"]["aws"]["enabled"]:
            cloud_integration.upload_to_s3(video_path, config["cloud"]["aws"]["bucket_name"])
            logger.info("Uploaded video to AWS S3.")
        if config["cloud"]["google"]["enabled"]:
            cloud_integration.upload_to_google_drive(video_path, config["cloud"]["google"]["folder_id"])
            logger.info("Uploaded video to Google Drive.")
        if config["cloud"]["nextcloud"]["enabled"]:
            cloud_integration.upload_to_nextcloud(video_path)
            logger.info("Uploaded video to Nextcloud.")
    except Exception as e:
        logger.error(f"Error uploading video to cloud: {e}")

def main():
    try:
        # Initialize modules
        motion_detector = MotionDetector(config["motion_detection"])
        face_recognizer = FaceRecognition(config["face_recognition"])
        video_recorder = VideoRecorder(config["video"])
        notifier = Notifier(config["notifications"])
        cloud_integration = CloudIntegration(config["cloud"])
        fall_detector = FallDetection(config["fall_detection"]["model_path"])
        encryption_manager = EncryptionManager(config["privacy"]["encryption_key"])
        voice_control = VoiceControl()
        sensor_manager = SensorManager(config["sensors"])
        energy_manager = EnergyManager(config["energy_management"])

        # Initialize Telegram Notifier
        telegram_notifier = TelegramNotifier(
            api_token=config["telegram"]["api_token"],
            chat_id=config["telegram"]["chat_id"])
        telegram_notifier.send_message("Home Security System has started successfully!")

        # Set up two-way audio (optional)
        two_way_audio = None
        if config["audio"]["enabled"]:
            try:
                two_way_audio = TwoWayAudio(config["audio"]["host"], config["audio"]["port"])
                logger.info("Two-Way Audio initialized.")
            except Exception as e:
                logger.error(f"Error initializing Two-Way Audio: {e}")

        logger.info("System initialized. Listening for activity...")

        while True:
            # Listen for voice commands
            command = voice_control.listen_for_command()
            if command == "arm":
                logger.info("System armed.")
            elif command == "disarm":
                logger.info("System disarmed.")
                continue  # Skip all processes until re-armed

            # Check motion
            if motion_detector.detect_motion():
                logger.info("Motion detected.")
                telegram_notifier.send_message("Alert: Motion detected in the monitored area.")

                # Check sensors for additional information
                sensor_status = sensor_manager.check_sensors()
                logger.info(f"Sensor statuses: {sensor_status}")

                # Capture frame for analysis
                frame = motion_detector.get_last_frame()
                if frame is None:
                    continue

                # Fall detection
                if fall_detector.detect_fall(frame):
                    logger.warning("Fall detected!")
                    notifier.send_alert("Fall detected in the monitored area.")
                    telegram_notifier.send_message("Alert: Fall detected in the monitored area!")

                # Perform face recognition
                if not face_recognizer.recognize_face(frame):
                    logger.info("Unknown face detected.")

                    # Record video
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    video_path = os.path.join(config["video"]["output_dir"], f"video_{timestamp}.mp4")
                    video_recorder.record_video(video_path, duration=config["video"]["duration"])
                    logger.info(f"Video recorded: {video_path}")

                    # Notify user and upload
                    notifier.send_alert("Unknown person detected!", attachment=video_path)
                    telegram_notifier.send_message("Alert: Unknown person detected!")
                    if os.path.exists(video_path):
                        telegram_notifier.send_file(video_path, caption="Suspicious activity recorded.")
                    
                    # Offload encryption and upload
                    threading.Thread(target=encrypt_and_upload, args=(video_path, config, encryption_manager, cloud_integration)).start()

            # Optional: Enable two-way audio
            if config["audio"]["enabled"] and two_way_audio:
                logger.info("Starting two-way audio communication.")
                two_way_audio.start_audio_stream()

    except KeyboardInterrupt:
        logger.info("System shutting down.")
    except Exception as e:
        logger.critical(f"Unexpected error: {e}")
    finally:
        if two_way_audio:
            two_way_audio.stop_audio_stream()
        logger.info("Resources cleaned up.")

if __name__ == "__main__":
    main()

