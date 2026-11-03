import cv2
import os
from datetime import datetime

def capture_image(frame):

    project_folder = os.path.dirname(os.path.abspath(__file__))
    capture_folder = os.path.join(project_folder, "captures")

    os.makedirs(capture_folder, exist_ok=True)

    filename = datetime.now().strftime("capture_%Y%m%d_%H%M%S_%f.jpg")
    filepath = os.path.join(capture_folder, filename)

    cv2.imwrite(filepath, frame)

    print("IMAGE SAVED:", filepath)