# AI Body Analyzer

An AI-powered web application that predicts body fat percentage using machine learning and provides basic body composition insights.

## Problem

Body composition analysis typically requires specialized machines available in clinics or gyms. This project explores a simpler, data-driven approach using basic body measurements.

## Features

* Predicts body fat % using a trained ML model
* Calculates BMI, ideal weight, and body metrics
* Displays actual vs ideal comparison
* Provides simple health insights

## Approach

User inputs body measurements → data is scaled → regression model predicts body fat % → system generates insights based on thresholds.

## Tech Stack

* Python
* Scikit-learn
* Streamlit
* Pandas, NumPy

## Dataset

Used a body fat dataset (252 samples) containing features like age, weight, height, and body measurements (abdomen, chest, hip, etc.).
Selected relevant features and trained model after preprocessing.

## Results

Tested Linear Regression and Random Forest.
Linear Regression performed better due to small dataset size and better generalization.

## Future Improvements

* Collect real-world data for better accuracy
* Add user profile and progress tracking
* Integrate computer vision for automated measurements
* Provide personalized recommendations using AI

 