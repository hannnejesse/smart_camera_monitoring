import cv2

def detect_motion(previous_frame, current_frame):
    difference = cv2.absdiff(previous_frame, current_frame)

    gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

    _, threshold = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

    motion_pixels = cv2.countNonZero(threshold)

    if motion_pixels > 500:
        return True

    return False