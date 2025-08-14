# 🌲 **Forest Monitoring & Deforestation Detection Web App**  

## 📌 **Problem Statement**  
Deforestation and carbon sequestration significantly influence climate change. Current monitoring methods are often **slow, resource-intensive, and inconsistent**, making it difficult to track and forecast forest health.  

This project introduces a **GIS-driven, automated deep learning system** that leverages **Sentinel-2 satellite imagery** to:  
- Detect ongoing deforestation activities  
- Estimate carbon sequestration capacity  
- Predict future forest health trends  

By providing accurate and scalable monitoring, the platform empowers conservationists, researchers, and policymakers worldwide.  

---

## 🎯 **Project Objectives**  

1. **Sentinel-2 Based Monitoring**  
   - Analyze satellite images (2019–2024) for **Igatpuri** and **Anjaneri** regions.  

2. **CNN-Powered Change Detection**  
   - Utilize **Convolutional Neural Networks** for precise vegetation change detection and prediction.  

3. **Interactive Web Platform**  
   - Build a **Django-based interface** for image upload, vegetation change visualization, and result downloads.  

4. **Change Detection & Trend Analysis**  
   - Detect vegetation gain, loss, water bodies, and no-change areas, along with long-term environmental trend analysis.  

---

## 🚀 **Key Features**  

- **Upload & Process** Sentinel-2 `.tif` satellite images  
- Detect:  
  - 🌿 Vegetation Gain  
  - 🔥 Vegetation Loss  
  - ⚪ No Change  
  - 💧 Water Bodies  
- **Region-specific thresholds** for Anjaneri & Igatpuri  
- **Interactive result visualization** with downloadable `.tif` output masks  
- **User-friendly UI** for accessibility  

---

## 🧑‍💻 **Technologies Used**  

- **Python**, **NumPy**, **Rasterio**, **Matplotlib**  
- **Django** (Backend + Web Interface)  
- **Sentinel-2 Imagery** (ESA Copernicus Open Access Hub)  
- **CNN Model** for pixel-wise classification and prediction  

---

## 🛠️ **Setup Instructions**  

### 1️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```
### 2️⃣ Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 3️⃣ Run the Development Server
```bash
python manage.py runserver
```
---
## 📂 Project Structure
``` bash
├── myproject/                # Main Django project folder
├── static/                   # CSS, JS, and static assets
├── templates/                # HTML templates
├── requirements.txt          # Dependencies
├── manage.py                  # Django management script
└── README.md                  # Project documentation
```
---
## 📜 License
This project is licensed under the MIT License — feel free to use, modify, and distribute with attribution.