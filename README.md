# 🌲 Forest Monitoring & Deforestation Detection Web App

## 📌 Problem Statement

Deforestation and carbon sequestration are critical drivers of climate change. Yet, current methods for monitoring forest health are slow, unevenly distributed, and resource-intensive. Traditional practices struggle to track forest land changes over time, leading to ineffective forecasting of future forest trends.

To address this, our project proposes a **GIS-driven, automated deep learning system** that uses **Sentinel-2 satellite imagery** to:
- Detect deforestation activities,
- Assess carbon sequestration capacity,
- Predict future forest health trends.

This platform aims to empower global conservation efforts through consistent, accurate, and scalable forest monitoring.

---

## 🎯 Project Objectives

1. **Sentinel-2 Based Monitoring:**  
   Analyze satellite images from **2019 to 2024** for monitoring forest regions in **Igatpuri** and **Anjaneri**.

2. **CNN-Powered Insight Extraction:**  
   Use a **Convolutional Neural Network (CNN)** to extract insights from satellite images for accurate forest change detection and prediction.

3. **Web-Based Platform:**  
   Provide an easy-to-use **Django-based web interface** to upload satellite images, visualize vegetation change, and download results.

4. **Change Detection & Trend Analysis:**  
   Compare historical and current data to detect vegetation gain, loss, and water bodies, and analyze environmental trends over time.

---

## 🚀 Features

- Upload and analyze Sentinel-2 satellite images (.tif format).
- Detect:
  - 🌿 Vegetation Gain
  - 🔥 Vegetation Loss
  - ⚪ No Change
  - 💧 Water Bodies
- Interactive result display and downloadable output (.tif mask).
- Region-specific processing logic (e.g., thresholds for Anjaneri and Igatpuri).
- Clean, user-friendly UI.

---

## 🧑‍💻 Technologies Used

- **Python**, **NumPy**, **Rasterio**, **Matplotlib**
- **Django** (Backend + Web Interface)
- **Sentinel-2 Imagery** (Satellite data source)
- **CNN Model** (for pixel classification and trend prediction)

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/forest-monitoring-app.git
   cd forest-monitoring-app

## 🛠️ Setup Instructions

### 🔧 Requirements Installation

```bash
pip install -r requirements.txt


###  🧱 Make Migrations

python manage.py makemigrations
python manage.py migrate

### 🚀 Run the Development Server
python manage.py runserver
