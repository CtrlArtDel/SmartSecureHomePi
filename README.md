# SmartSecure Pi: AI-Powered Home Security System

## Overview

**SmartSecure Pi** is an AI-powered, low-resource home security system designed to ensure safety and efficiency. It integrates advanced features such as motion detection, face recognition, fall detection, real-time notifications, cloud storage, and voice control. The system is modular, scalable, and optimized for low power consumption.

## Features

**Motion Detection**:
- Detects movement using a PIR sensor and triggers appropriate actions.
- Logs motion events and idle states.

 **Face Recognition**: 
 - Identifies known faces for security purposes and logs any unknown face detections.
  
 **Fall Detection**: 
 - Uses AI to detect falls or unusual body movements, with real-time alerts.
  
 **Real-Time Notifications**: 
 - Sends alerts via **Telegram**, **email**, and **push notifications**.
 - Logs notification events.
 
 **Cloud Integration**: 
 - Uploads recorded videos to **AWS S3**, **Google Drive**, or **Nextcloud** for backup and easy access.
 - Logs cloud storage operations.

 **Two-Way Audio**:
 - Supports communication with visitors through audio streaming.
  
 **Voice Control**: 
 - Arms or disarms the system using voice commands.

 **Energy Management**: 
 - Optimizes power consumption by switching to low-power modes when idle.

 **Privacy**: 
 - Encrypts local video storage with AES encryption.


## Project Structure
```cpp
SmartSecure_Pi/
├── config/
│   ├── __init__.py 
│   ├── config.yaml          # Configuration settings for the project
│   ├── secrets.yaml         # Sensitive credentials (e.g., API keys, passwords)
├── data/
│   ├── faces/               # Face recognition training data
│   ├── logs/                # System logs for debugging and monitoring
├── models/
│   └── fall_detection.tflite # Pre-trained fall detection model
├── src/
│   ├── ai/                   # AI-related modules (face recognition, fall detection)
│   |   ├── __init__.py 
│   │   ├── face_recognition_module.py
│   │   ├── fall_detection.py
│   ├── audio/                # Audio-related modules (voice control, two-way audio)
│   |   ├── __init__.py 
│   │   ├── audio_communication.py
│   │   ├── voice_control.py
│   ├── notifications/        # Notification-related modules (email, push, telegram)
│   |   ├── __init__.py 
│   │   ├── notifications.py
│   │   ├── telegram_notifier.py
│   ├── sensors/              # Motion detection and sensor management
│   |   ├── __init__.py 
│   │   ├── motion_detection.py
│   │   ├── sensor_manager.py
│   ├── storage/              # Video recording, encryption, cloud integration
│   |   ├── __init__.py 
│   │   ├── video_recorder.py
│   │   ├── encryption_manager.py
│   │   ├── cloud_integration.py
│   ├── system/               # System-level functionality (energy management)
│   |   ├── __init__.py 
│   │   ├── energy_manager.py
│   ├── utilities/            # Utility modules (logging)
│   |   ├── __init__.py 
│   │   ├── logger.py         # Centralized logging
│   ├── main.py               # Main entry point for the system
├── tests/
│   ├── test_motion_detection.py
│   ├── test_face_recognition.py
│   ├── test_fall_detection.py
│   ├── test_cloud_integration.py
│   ├── test_audio_communication.py
│   ├── test_notifications.py
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
```

Installation

1. **Clone the Repository**
Clone the repository to your local machine:

```cpp
git clone https://github.com/your-repository/smartsecure_Pi.git
cd smartsecure_Pi
```

2. **Set Up a Virtual Environment**
   
It’s recommended to use a virtual environment to manage dependencies.

```cpp
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```cpp
pip install -r requirements.txt
```

4. **Set Up Configuration Files**
   
Edit the `config/config.yaml` and `config/secrets.yaml` files with your specific configuration, API keys, and secrets.


6. **Run the Application**
   
```cpp
python src/main.py
```

## Logging
The system uses centralized logging for tracking activity and debugging. Logs are stored in `data/logs/system.log` and are displayed in the console.

Log Levels:
`INFO`: General operational messages (e.g., system initialization, events).
`DEBUG`: Detailed messages useful for development.
`ERROR`: Error messages for issues requiring attention.
`CRITICAL`: Severe errors that might stop the system.
Logs are also written to `data/logs/system.log` and can be rotated based on the configuration.

## Features in Detail

**Motion Detection**
- Uses a PIR sensor to detect movement.
- Logs motion detection events and system idle state.

**Face Recognition**
- Detects known faces and logs any unfamiliar faces.
- Supports real-time alerts for unauthorized access.

**Fall Detection**
- Monitors unusual movements or falls.
- Logs fall detection events and sends alerts.

**Cloud Storage Integration**
- Uploads recorded videos to cloud services like AWS S3, Google Drive, or Nextcloud.
- Supports encryption of videos before uploading.

**Voice Control and Two-Way Audio**
- Arms or disarms the system using voice commands.
- Supports real-time communication with visitors using audio.

**Energy Management**
- Optimizes system power usage by switching to low-power mode when idle.

## Testing

**1. Unit Tests**
Run unit tests using `pytest` to ensure all modules work correctly:

```cpp
pytest
```

**2. Manual Tests**
Test specific components by running individual test scripts:


```cpp
python tests/test_motion_detection.py
python tests/test_face_recognition.py
```

## License
This project is licensed under the MIT License. See LICENSE for details.

