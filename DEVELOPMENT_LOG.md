# Smart Camera Monitoring — Development Log

## Project Overview

**Goal:** Develop a smart camera monitoring system for dusty rice-storage environments.

**Main features:**
- Activity-triggered image capture.
- Avoid unnecessary continuous capture.
- Detect possible dust or reduced image visibility.
- Automatically clean the camera's protective window.
- Evaluate two prototypes: ESP32-S3 and Raspberry Pi 5.

## Development Environment

- Operating system: Windows
- Code editor: Visual Studio Code
- Version control: Git
- Remote repository: GitHub
- ESP32-S3 simulation: Wokwi browser
- Physical hardware: Not available during initial software development

## Initial Setup History

### 1. Git and repository setup

- Verified Git installation.
- Created a local Git repository in `smart_camera_monitoring`.
- Connected the local repository to the GitHub repository.
- Corrected the remote URL to use the repository name `smart_camera_monitoring`.
- Retrieved the existing GitHub README.
- Renamed the local branch from `master` to `main`.
- Verified that the working tree was clean.

### 2. Project folder setup

- Renamed the local `main` folder to `prototype-esp32s3`.
- Confirmed that Git reported a clean working tree.
- Note: Git does not track empty folders.

### 3. Wokwi setup

- Installed the Wokwi Simulator extension in VS Code.
- Activated the Wokwi license.
- Encountered a missing workspace configuration message.
- Created initial `diagram.json` and `platformio.ini` files.
- Removed `wokwi.toml` after deciding to use browser-based Wokwi.
- Selected browser-based Wokwi to reduce setup complexity.
- Important: Browser Wokwi files do not automatically synchronize with the local repository.

## Current Status

- GitHub repository connection: Verified by successful fetch.
- Local branch: `main`.
- Existing README: Present.
- Development log: Created.
- ESP32-S3 simulation: Not yet tested.
- Activity-triggered capture logic: Not yet implemented.
- Automatic lens-cleaning logic: Not yet implemented.
- Raspberry Pi 5 prototype: Not yet started.

## Record-Keeping Rules

For each development step, record:
- Date and step number.
- Objective and reason for the change.
- Files and settings changed.
- Commands or procedures used.
- Expected and actual results.
- Test status: PASS, FAIL, or NOT TESTED.
- Errors, troubleshooting, and corrective actions.
- Git commit identifier after the change is committed.

## Test 001 — ESP32-S3 Basic Boot and Serial Test

**Date:** 2026-10-18

### Objective
Verify that the ESP32-S3 Wokwi simulation boots correctly and that the firmware can print status messages through the Serial Monitor.

### Test Setup
- Platform: Wokwi browser
- Target: ESP32-S3 DevKitC-1 simulation
- Firmware file: `sketch.ino`
- Serial baud rate: 115200
- Test interval: 2000 ms

### Test Procedure
1. Started the ESP32-S3 Wokwi simulation.
2. Opened the Serial Monitor.
3. Observed the ESP32 boot messages.
4. Verified the application startup message.
5. Verified repeated monitoring messages.

### Expected Result
The ESP32-S3 should boot and continuously print:

`Smart Camera Monitoring Started`

followed by:

`Monitoring for activity...`

approximately every 2 seconds.

### Actual Result
The ESP32-S3 booted successfully.

Observed output included:

`Smart Camera Monitoring Started`

`Monitoring for activity...`

The monitoring message continued to repeat.

### Result
**PASS**

### Notes
The ESP32-S3 simulation, firmware startup, serial communication, and continuous loop operation are functioning correctly.

### Next Step
Implement the first activity-trigger input and test event-driven monitoring instead of continuous status reporting.

## Test 002 — PIR Activity Trigger Setup

### Objective
Add a PIR motion sensor as the first activity-trigger input for the ESP32-S3 prototype.

### Component
- Sensor: HC-SR501 PIR motion sensor
- Controller: ESP32-S3-DevKitC-1

### Connections
| PIR Pin | ESP32-S3 Pin | Function |
|---|---|---|
| VCC | 5V | Sensor power |
| OUT | GPIO4 | Digital activity signal |
| GND | GND | Common ground |

### Design Reason
The PIR is being used as the first simulation method for detecting activity. The purpose is to test an event-driven capture architecture before introducing the camera and image-processing stages.

### Current Status
PIR hardware setup completed in Wokwi.

### Test Status
NOT TESTED — firmware has not yet been modified to read GPIO4.

- Result: PASS
- Simulation: Wokwi
- Startup messages appeared correctly.
- Triggered motion using the Wokwi PIR sensor's "Trigger Motion" control.
- ESP32-S3 printed "ACTIVITY DETECTED".
- Event detection worked on a LOW-to-HIGH transition.

### Next Step
Modify the ESP32-S3 firmware to monitor GPIO4 and report activity detection through the Serial Monitor.

### Next Step
Develop the camera activation logic following successful PIR activity detection.

## Test 003 — Motion-Triggered Camera Activation Indicator

### Objective
Activate an LED when the PIR sensor detects motion, representing the camera activation signal.

### Hardware Configuration
- Controller: ESP32-S3-DevKitC-1
- PIR sensor output: GPIO4
- Camera activation indicator: GPIO5
- LED resistor: 220 ohms

### Firmware Changes
- Added GPIO5 as an output.
- Added LED activation when PIR changes from LOW to HIGH.
- Added LED deactivation when PIR returns from HIGH to LOW.

### Test Environment
- Wokwi simulation

### Test Result
- Result: PASS
- Motion detection message appeared.
- Camera activation signal ON appeared.
- Camera activation signal OFF appeared.
- Multiple motion events were detected successfully.

### Limitation
The LED represents the camera activation signal. Actual camera capture has not yet been implemented.

### Next Step
Develop the camera capture workflow and investigate ESP32-S3 camera simulation options.

## Test 004 — Motion-Triggered Camera Capture Request

### Objective
Generate a simulated camera capture request when motion is detected.

### Firmware Changes
- Added CAMERA CAPTURE REQUESTED serial message.
- Retained GPIO5 LED activation and deactivation.
- Retained GPIO4 PIR motion detection.

### Test Environment
Wokwi ESP32-S3 simulation.

### Test Result
PASS
- Activity detected successfully.
- Camera activation signal ON.
- Camera capture request generated.
- Camera activation signal OFF.

### Limitation
This test generates a simulated capture request. Actual image capture is not implemented or verified.

### Next Step
Add event monitoring and event counting.

## Test 005 — Motion Event Counting

### Objective
Count each new motion detection event.

### Firmware Changes
- Added motionEventCount variable.
- Incremented the counter on each LOW-to-HIGH transition.
- Printed the event number in Serial Monitor.

### Test Environment
Wokwi ESP32-S3 simulation.

### Test Result
PASS
- First motion event counted as 1.
- Second motion event counted as 2.
- Capture request generated for both events.
- LED switched OFF between events.

### Limitation
Event count resets when the ESP32 restarts. Events are not permanently stored.

### Next Step
Perform complete integration testing.

## Test 006 — Dust Protection Design

### Objective
Define a protection concept for the camera in a dusty rice-barn environment.

### Proposed Design
- Enclosed camera housing to reduce dust exposure.
- Transparent protective window in front of the lens.
- Removable window for cleaning and maintenance.
- Small soft-brush mechanism to remove accumulated dust.
- Camera activation only when motion is detected to reduce unnecessary operation.

### Test Status
Design documented only. No physical enclosure or cleaning mechanism has been built or tested.

### Next Step
Final GitHub review and project completion.

## Final ESP32-S3 Wokwi Verification

### Test Results
- PIR motion detection: PASS
- Motion event counter: PASS
- LED ON during motion: PASS
- LED OFF after motion stops: PASS
- Simulated camera capture request: PASS

### Verification
The complete ESP32-S3 simulation was successfully tested in Wokwi.

### Limitations
Actual camera capture and physical hardware testing are pending.


## Raspberry Pi 5 Prototype – Development Progress

### Environment Setup
- Python 3.14.10 installed successfully.
- pip verified.
- OpenCV 5.0.0 installed and import tested successfully.
- NumPy 2.5.4 installed.
- VS Code Python extension installed.

### Initial Development
- Created `prototype-raspberry-pi5/main.py`.
- Verified Python program execution successfully.
- Created `prototype-raspberry-pi5/motion_detection.py` for frame-difference-based motion detection.
- Created `prototype-raspberry-pi5/camera.py` for timestamped image storage.

### Current Status
- Python environment: PASS
- OpenCV import: PASS
- Initial Python program: PASS
- Motion detection module: CREATED – testing pending
- Camera image-saving module: CREATED – testing pending
- End-to-end integration: PENDING
- Physical Raspberry Pi 5 and camera testing: PENDING

### Development Limitation
Development is currently being performed on Windows using simulated camera input. Actual Raspberry Pi 5 hardware and camera operation have not yet been tested.

## Raspberry Pi 5 – Image Storage and Git Configuration

### Image Storage
- Updated camera.py to save images inside the prototype-raspberry-pi5/captures directory.
- Verified timestamp-based JPG image creation.
- Confirmed the captured image is visible and accessible.

### Git Configuration
- Created a root-level .gitignore file.
- Added rules to ignore Python cache files.
- Added rules to ignore generated captures folders.
- Verified generated image folders no longer appear as untracked files.

### Verification
- Correct image storage location: PASS
- JPG image creation: PASS
- Python cache ignore rule: CONFIGURED
- Generated capture folder ignore rule: CONFIGURED

### Current Limitation
Camera input is simulated using generated image frames on Windows. Physical Raspberry Pi 5 camera testing remains pending.

## Raspberry Pi 5 – Multi-Event Motion Detection Test

- Implemented simulation of multiple camera frames.
- Tested two separate movement events with periods of no motion between them.
- Motion detection successfully identified 2 separate events.
- Each event triggered an image capture request.
- Fixed image filename collision by adding microseconds (`%f`) to timestamps.
- Verified that two separate JPG images were saved in `prototype-raspberry-pi5/captures/`.

**Test Result: PASS**

**Limitation:** Tested using simulated frames on Windows with Python and OpenCV. Physical Raspberry Pi 5 and camera testing is pending.