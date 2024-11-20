import cv2
import os
import datetime

class VideoRecorder:
    def __init__(self, camera_config):
        self.resolution = tuple(camera_config['resolution'])
        self.framerate = camera_config['framerate']

    def record_video(self, duration=10, save_path="/home/pi/videos"):
        os.makedirs(save_path, exist_ok=True)
        filename = os.path.join(save_path, f"{datetime.datetime.now().isoformat()}.avi")

        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolution[0])
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolution[1])
        cap.set(cv2.CAP_PROP_FPS, self.framerate)

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, fourcc, self.framerate, self.resolution)

        start_time = datetime.datetime.now()
        while (datetime.datetime.now() - start_time).seconds < duration:
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)

        cap.release()
        out.release()
        return filename

