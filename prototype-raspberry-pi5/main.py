import cv2
import numpy as np

from motion_detection import detect_motion
from camera import capture_image

print("SMART CAMERA MONITORING")
print("Raspberry Pi 5 Prototype")
print("Continuous Monitoring Started")

# Create an empty camera frame
blank_frame = np.zeros((480, 640, 3), dtype=np.uint8)

# Generate simulated camera frames
frames = []

# No motion
frames.extend([blank_frame.copy()] * 3)

# First movement
for x in [50, 70, 90]:
    frame = blank_frame.copy()
    cv2.rectangle(frame, (x, 100), (x + 50, 150),
                  (255, 255, 255), -1)
    frames.append(frame)

# No motion
frames.extend([blank_frame.copy()] * 3)

# Second movement
for x in [150, 170, 190]:
    frame = blank_frame.copy()
    cv2.rectangle(frame, (x, 200), (x + 50, 250),
                  (255, 255, 255), -1)
    frames.append(frame)

previous_frame = frames[0]
motion_active = False
event_count = 0

# Continuous monitoring simulation
for current_frame in frames[1:]:

    motion_detected = detect_motion(
        previous_frame, current_frame
    )

    if motion_detected and not motion_active:

        event_count += 1

        print("MOTION EVENT:", event_count)
        print("CAPTURE REQUESTED")

        capture_image(current_frame)

        motion_active = True

    elif not motion_detected:
        motion_active = False

    previous_frame = current_frame

print("Monitoring completed.")
print("TOTAL MOTION EVENTS:", event_count)