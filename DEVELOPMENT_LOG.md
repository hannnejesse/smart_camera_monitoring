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

