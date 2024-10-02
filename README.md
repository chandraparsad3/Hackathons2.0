# IoT-Based Fungus Detection System - Protecting Health and Saving Lives

Fungal spores in the air pose serious health risks, especially for those with respiratory conditions like asthma, allergies, or compromised immune systems. Prolonged exposure to mold can lead to severe health complications, and in some cases, life-threatening infections. To address this issue, we've developed an innovative **IoT-based Fungus Detection System**. This system provides early warnings about potential fungal growth in indoor environments, offering a proactive solution to safeguard human health by preventing exposure to harmful airborne fungi.

By leveraging cutting-edge sensor technology, machine learning, and real-time alerts, the system can significantly reduce health risks associated with fungal contamination, making it invaluable for homes, greenhouses, hospitals, and any space where air quality is critical.

## Tools, Technologies, and Frameworks

The IoT-based Fungus Detection System integrates a combination of hardware and software to monitor environmental conditions and detect fungal risks:

### Hardware:
- **MQ135 and MQ7 Sensors:** Measure harmful gases like CO2, NH3, and carbon monoxide, often associated with poor air quality and fungal presence.
- **DHT11 Sensor:** Tracks temperature and humidity—key factors in fungal growth.
- **LDR (Light Dependent Resistor):** Monitors light intensity, as certain fungi thrive in low-light conditions.

### Software:
- **Flask Framework:** A lightweight web framework used to create a user-friendly interface and API for data interaction.
- **Machine Learning (Logistic Regression):** A trained model processes sensor data to predict the likelihood of fungal growth, enabling early intervention.
- **Twilio API:** Sends SMS alerts to users when environmental conditions indicate potential fungal threats.
- **Kindwise API:** Provides image-based fungus identification, allowing users to upload images of suspected mold and receive accurate species detection and advice.

## Installation and Setup

### 1. Create a Virtual Environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 2. Install Required Packages:
```bash
pip install Flask numpy scikit-learn requests twilio
```

### 3. Place Model Files:
Add the pre-trained machine learning model (`log.pkl`) and scaler (`scaler.pkl`) into the `fungus/models/` directory for prediction use.

### 4. Run the Application:
```bash
flask run
```

The sensors are connected to the system via **Arduino** or **Raspberry Pi** to collect real-time data, ensuring continuous monitoring of the environment.

## Problem Statement and Real-World Impact

Mold and fungi thrive in environments with specific conditions—high humidity, low ventilation, poor air quality, and darkness. These fungi release spores into the air, which can lead to significant health issues when inhaled, especially for vulnerable individuals. Current methods of detecting mold are mostly reactive, meaning that by the time mold is discovered, it has already grown and potentially impacted people's health.

Our **IoT-based Fungus Detection System** offers a proactive solution. The system continuously monitors environmental conditions using sensors to detect rising humidity, temperature, and harmful gas concentrations—key factors for fungal growth. When these thresholds are met, the system analyzes the data using a machine learning model and sends immediate SMS alerts, allowing users to take preventive action before mold and fungus can develop.

The inclusion of **MQ135** and **MQ7** sensors enhances the system’s precision by detecting poor air quality conditions, ensuring early detection of environments at risk for fungal growth. Furthermore, users can upload images of potential mold, and the system will identify the fungal species, providing steps to mitigate its growth.

By utilizing this technology, we aim to prevent mold infestations, improve air quality, and most importantly, protect the health and well-being of individuals. This system is not just an innovation—it's a vital tool for saving lives and ensuring safe living environments.

## Features
- **Real-time monitoring** of temperature, humidity, harmful gases, and light intensity.
- **Machine learning-based prediction** of fungal growth.
- **SMS alerts** for early warnings of fungal risks.
- **Image-based fungus identification** through the Kindwise API.
