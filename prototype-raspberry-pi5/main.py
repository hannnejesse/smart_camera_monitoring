import cv2
import numpy as np

from motion_detection import detect_motion
from camera import capture_image

print("SMART CAMERA MONITORING")
print("Raspberry Pi 5 Prototype")
print("System Started Successfully")

# Simulate two camera frames
previous_frame = np.zeros((480, 640, 3), dtype=np.uint8)

current_frame = previous_frame.copy()

# Simulate movement in the second frame
cv2.rectangle(current_frame, (100, 100), (200, 200), (255, 255, 255), -1)

print("Checking for motion...")

# Detect motion
motion_detected = detect_motion(previous_frame, current_frame)

if motion_detected:
    print("MOTION DETECTED!")
    print("Triggering image capture...")
    capture_image(current_frame)
else:
    print("No motion detected.")

print("Monitoring test completed.")