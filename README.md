# 🛣️ SafeTrack - IoT Vehicle Tracking & Theft Prevention System 🛡️

## 📌 Overview

SafeTrack is an IoT-based Vehicle Tracking and Theft Prevention System designed to provide real-time vehicle monitoring, geofence-based security, theft detection, and location history tracking.

The project simulates an intelligent vehicle security platform using Python and Streamlit, making it suitable for both hardware-based implementation and virtual IoT environments.

This system continuously tracks vehicle location, detects unauthorized movement, generates theft alerts, and visualizes tracking data through a modern cyber-themed dashboard.

---

## 🚀 Key Features

### 📍 Real-Time Vehicle Tracking

* Live GPS coordinate monitoring
* Continuous location updates
* Google Maps integration

### 🛡️ Theft Prevention

* Geofence boundary monitoring
* Unauthorized movement detection
* Theft alert generation

### 📊 Smart Dashboard

* Modern Streamlit dashboard
* Live vehicle status monitoring
* Alert analytics
* Tracking history visualization

### 📈 Data Logging

* Timestamp-based tracking logs
* CSV report generation
* Historical movement analysis

### 🌐 IoT Architecture

* GPS Simulation / GPS Module
* ESP32 Integration Ready
* Cloud Dashboard Ready
* Real-Time Monitoring

---

## 🎯 Problem Statement

Vehicle theft and lack of real-time monitoring remain major challenges for vehicle owners, logistics companies, transportation services, and fleet operators.

SafeTrack addresses these challenges by providing:

* Continuous vehicle location tracking
* Geofence-based monitoring
* Theft detection alerts
* Historical location logging
* Centralized monitoring dashboard

---

## 🏗️ System Architecture

GPS Module / GPS Simulator
↓
ESP32 / Python Processing Engine
↓
Location Tracking Engine
↓
Geofence Detection System
↓
Alert Generation Module
↓
CSV Data Storage
↓
Streamlit Dashboard
↓
User Monitoring Interface

---

## ⚙️ Technology Stack

### Programming Language

* Python 3.x

### Dashboard

* Streamlit

### Data Processing

* Pandas

### Visualization

* Streamlit Maps
* Interactive Analytics

### Storage

* CSV Logging

### Hardware (Optional)

* ESP32
* Neo-6M GPS Module
* Buzzer
* Relay Module
* GSM Module

---

## 📂 Project Structure

```text
SafeTrack-IoT-Vehicle-Tracking-Theft-Prevention-System/

│
├── arduino_code/
├── python_simulation/
├── dashboard/
│   └── app.py
├── data/
│   └── log.csv
├── outputs/
├── reports/
├── images/
├── docs/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 Project Workflow

1. Generate GPS coordinates
2. Monitor vehicle movement
3. Check geofence boundaries
4. Detect suspicious activity
5. Generate alerts
6. Store tracking records
7. Visualize data on dashboard

---

## 🛠️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/SafeTrack-IoT-Vehicle-Tracking-Theft-Prevention-System.git

cd SafeTrack-IoT-Vehicle-Tracking-Theft-Prevention-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Step 1: Start Vehicle Tracking

```bash
python main.py
```

This will:

* Simulate GPS coordinates
* Detect geofence breaches
* Generate theft alerts
* Store logs in CSV

### Step 2: Launch Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

## 📊 Dashboard Features

* Futuristic Cyber-Themed UI
* Live Vehicle Status
* GPS Location Monitoring
* Alert Detection Panel
* Tracking History Logs
* CSV Report Download
* Interactive Location Map

---

## 📍 Sample Output

### Safe Vehicle

```text
Location: 8.531390
Longitude: 76.909667

Status: SAFE
Alert: NONE
```

### Theft Alert

```text
Location: 8.573959
Longitude: 76.921848

Status: THEFT ALERT
Alert: GEOFENCE BREACH
```

---

## 📈 Future Enhancements

* Live GPS Hardware Integration
* MQTT Communication
* Node-RED Dashboard
* Mobile Application
* SMS Alert System
* Email Notifications
* Vehicle Engine Lock Feature
* Cloud Database Integration
* AI-Based Theft Prediction
* Route Optimization

---

## 🎓 Learning Outcomes

This project demonstrates knowledge of:

* Internet of Things (IoT)
* Real-Time Monitoring Systems
* GPS Tracking Technologies
* Geofencing
* Cybersecurity Concepts
* Data Logging
* Dashboard Development
* Python Programming
* Streamlit Development

---

## 💼 Industry Applications

* Fleet Management
* Logistics Tracking
* School Bus Monitoring
* Delivery Services
* Ride-Sharing Platforms
* Asset Tracking
* Vehicle Security Systems

---


