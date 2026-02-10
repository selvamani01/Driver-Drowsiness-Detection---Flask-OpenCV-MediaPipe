# 🚗 Driver Drowsiness Detection System (AI + Full Stack)

A real-time AI-powered Driver Monitoring System that detects driver drowsiness using Computer Vision and alerts to prevent accidents. Built with Flask, OpenCV, and MediaPipe, this project streams live video in a web interface and triggers an alert when signs of fatigue are detected.

---

## 📌 Project Overview

Driver fatigue is one of the major causes of road accidents worldwide. This project uses **facial landmark detection and Eye Aspect Ratio (EAR)** to monitor the driver's eye state in real time. If the system detects prolonged eye closure (drowsiness), it triggers an alert to warn the driver and reduce the risk of accidents.

---

## ✨ Features

- Real-time webcam monitoring
- Eye detection using MediaPipe FaceMesh
- Eye Aspect Ratio (EAR) based drowsiness detection
- Audio alert when driver is drowsy
- Live video streaming via Flask web app
- Modern dashboard UI (HTML + CSS + JS)
- Real-time EAR value display
- Non-blocking alert system
- Lightweight and fast

---

## 🧠 How It Works

1. Webcam captures live video.
2. MediaPipe detects facial landmarks.
3. Eye landmarks are extracted.
4. Eye Aspect Ratio (EAR) is calculated.
5. If EAR stays below threshold for certain frames → **Drowsiness detected**.
6. System triggers **alert sound** and warning message.

---

## 🛠️ Tech Stack

- **Python**
- OpenCV
- MediaPipe
- Flask (Backend)
- HTML, CSS, JavaScript (Frontend)
- Winsound (Alert system)

---

Future Improvements (Accident Prevention System)

This project can be extended into a Smart Driver Safety System:

🔹 Automatic vehicle braking when drowsiness detected

🔹 Integration with embedded systems (Raspberry Pi / Arduino)

🔹 Connect to vehicle CAN bus for real-time control

🔹 Steering vibration / seat vibration alert

🔹 GPS alert to emergency contact

🔹 Real-time driver health monitoring

🔹 Deep learning model for higher accuracy

🔹 Mobile app monitoring

🔹 Cloud logging and analytics

🔹 Multi-driver detection
