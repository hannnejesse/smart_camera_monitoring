import cv2
import os
from datetime import datetime

def capture_image(frame):

    os.makedirs("captures", exist_ok=True)

    filename = datetime.now().strftime("capture_%Y%m%d_%H%M%S.jpg")

    filepath = os.path.join("captures", filename)

    cv2.imwrite(filepath, frame)

    print("IMAGE SAVED:", filepath)