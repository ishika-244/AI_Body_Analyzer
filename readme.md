# 🧠 FitSense AI

Understand your body beyond just weight.

FitSense AI is a hybrid body composition analysis tool that estimates key health metrics like body fat, visceral fat, muscle mass, and body age using simple body measurements.

---

## 🚀 Live Demo
👉 https://aibodyanalyzer-mbsa55pudnlzwzxzhqekh5.streamlit.app/

---

## 📌 Problem Statement

Most people evaluate their health using only weight or BMI.

However, these metrics fail to capture actual body composition such as:
- Body Fat %
- Muscle Mass
- Visceral Fat

This leads to incomplete or misleading health insights.

FitSense AI solves this by providing a more comprehensive, accessible, and explainable body analysis without requiring expensive equipment.

---

## ✨ Features

- Hybrid body composition estimation (formula-based + ML-assisted)
- Calculates Body Fat %, BMI, Ideal Weight, Muscle Mass, Visceral Fat & Body Age
- Category-based health interpretation (Low / Ideal / High)
- Clean and interactive UI using Streamlit
- Instant results with actionable insights

---

## ⚙️ How It Works

1. User inputs body measurements (age, height, weight, circumferences)
2. Body fat is estimated using validated formulas (US Navy method)
3. Other metrics (BMI, visceral fat, muscle mass, body age) are computed using analytical models
4. Machine learning components are integrated where applicable
5. Results are presented with clear categories and insights

---

## 🧠 Key Insight

Unlike black-box models, FitSense AI focuses on:
- Explainability  
- Real-world usability  
- Interpretable health metrics  

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy  
- Streamlit  
- Scikit-learn (for ML components)  

---

## 📊 Dataset

- Body Fat Prediction Dataset (Kaggle)  
- Features used:
  - Age, Weight, Height  
  - Abdomen, Chest, Hip, Thigh, Neck  

---

## 🤖 Model

- Algorithm: Linear Regression  
- Preprocessing: StandardScaler  
- Note: ML model is integrated but primary predictions rely on validated domain formulas for better reliability.

---

## ⚠️ Disclaimer

This tool provides general fitness insights and is not a substitute for professional medical advice or clinical measurements (e.g., BIA, DEXA scans).

---

## 🔮 Future Improvements

- Personalized fitness and nutrition recommendations  
- Real-time measurement using computer vision  
- User history tracking and progress analysis  
- Improved calibration with real-world data  

---

