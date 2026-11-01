# Smart Camera Monitoring

## Project Overview
An event-triggered monitoring system designed for dusty environments such as rice storage barns. The system detects motion and generates a camera activation request instead of continuously monitoring.

## Current Prototype
- **Microcontroller:** ESP32-S3
- **Simulation:** Wokwi
- **Motion sensor:** HC-SR501 PIR
- **Output:** LED indicator
- **Programming:** Arduino C++

## Implemented Features
- PIR-based motion detection
- Motion event counting
- LED activation during detected motion
- Simulated camera capture request
- Event-based monitoring

## Pin Connections

| Component | ESP32-S3 |
|---|---|
| PIR OUT | GPIO 4 |
| PIR VCC | 5V |
| PIR GND | GND |
| LED control | GPIO 5 |

## Testing
The ESP32-S3 prototype was tested in Wokwi. Motion detection, event counting, LED activation/deactivation, and simulated camera activation requests were verified.

## Current Limitations
- Actual camera capture is not implemented.
- Image storage is not implemented.
- Physical hardware testing is pending.
- Dust-protection enclosure is a proposed design.

## Future Work
- Integrate a camera module.
- Implement image capture and storage.
- Develop dust-protection hardware.
- Build and test a physical ESP32-S3 prototype.
- Develop a Raspberry Pi 5 prototype for comparison.

## Repository Structure
- `prototype-esp32s3/sketch.ino` — ESP32-S3 firmware
- `prototype-esp32s3/diagram.json` — Wokwi circuit
- `DEVELOPMENT_LOG.md` — Development history and testing records
