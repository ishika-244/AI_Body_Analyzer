# AI Body Analyzer

Understand your real health beyond just weight.

AI-powered body composition analyzer that predicts body fat % 
and provides actionable health insights using simple body measurements.

## Live Demo

👉 https://aibodyanalyzer-mbsa55pudnlzwzxzhqekh5.streamlit.app/

## Problem Statement

Most people judge their health using only weight or BMI.

However, these metrics fail to capture actual body composition such as:
- Body fat %
- Muscle mass
- Visceral fat

This leads to misleading conclusions about health.

This project aims to provide a more complete and accessible body analysis 
without requiring expensive gym or clinical equipment.

## Features

- Predicts Body Fat % using Machine Learning
- Calculates BMI and Ideal Weight
- Estimates Muscle Mass and Visceral Fat
- Provides category-based health analysis
- Clean and interactive UI using Streamlit
- Instant results with actionable insights

## How It Works

1. User enters basic body measurements (age, height, weight, etc.)
2. Data is scaled using StandardScaler
3. Machine Learning model predicts body fat %
4. Additional health metrics are calculated
5. Results are displayed with categories and insights

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Joblib

## Dataset

- Body Fat Prediction Dataset (Kaggle)
- Features used:
  - Age, Weight, Height
  - Abdomen, Chest, Hip, Thigh, Neck

## Model

- Algorithm: Linear Regression
- Preprocessing: StandardScaler
- Output: Body Fat %
- Performance: Linear Regression performed better than Random Forest in this dataset

## Future Improvements

- Collect real-world user data for better model accuracy
- Add personalized diet and workout recommendations
- Integrate computer vision for automatic body measurement detection
- Add user login and history tracking
 