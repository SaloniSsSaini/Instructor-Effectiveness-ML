# Instructor Effectiveness Modeling using Machine Learning

## Overview

This project analyzes instructor performance in an EdTech learning platform using machine learning techniques.
The goal is to identify and predict instructor effectiveness levels based on learner engagement, learning outcomes, and feedback metrics.

The project includes data analysis, feature engineering, predictive modeling, explainable AI, and an interactive dashboard for visualization.

---

## Problem Statement

In large online learning platforms, it is difficult to evaluate instructor performance accurately. Traditional evaluation methods rely only on student feedback or completion rates.

This project uses a data-driven approach to measure instructor effectiveness by combining multiple indicators such as learner engagement, performance improvement, and feedback quality.

---

## Dataset

The dataset contains course batch-level data including:

* Batch ID
* Instructor ID
* Course ID
* Completion Rate
* Dropout Rate
* Average Quiz Score
* Average Score Improvement
* Watch Time
* Assignment Submission Rate
* Forum Activity Rate
* Feedback Score
* Feedback Response Rate

Each row represents a learning batch conducted by an instructor.

---

## Project Workflow

### 1. Data Loading

The dataset is loaded using Pandas and inspected to understand its structure and features.

### 2. Data Cleaning

Missing values are handled and numeric columns are prepared for analysis.

### 3. Exploratory Data Analysis (EDA)

EDA is performed to understand patterns in the data.

Visualizations include:

* Completion rate distribution
* Correlation heatmap
* Instructor effectiveness distribution

### 4. Feature Engineering

New features were created to capture deeper patterns in instructor performance.

**Engagement Score**
Average of:

* Watch time
* Assignment submission rate
* Forum activity rate

**Learning Score**
Average of:

* Score improvement
* Quiz score

**Feedback Quality**
Feedback score × response rate

---

## Instructor Effectiveness Score

A composite effectiveness score was calculated using a weighted formula:

Completion Rate: 30%
Learning Score: 20%
Engagement Score: 20%
Feedback Quality: 20%
Dropout Rate: -10%

This score was used to classify instructors into three tiers:

* Low
* Medium
* High

---

## Machine Learning Models

The following models were trained and compared:

* Random Forest
* Logistic Regression
* Gradient Boosting

Random Forest provided the best performance and was selected as the final model.

---

## Model Performance

The model achieved approximately **96% accuracy** in predicting instructor effectiveness tiers.

Evaluation metrics used:

* Accuracy Score
* Confusion Matrix
* Classification Report

---

## Explainable AI

SHAP (SHapley Additive Explanations) was used to interpret model predictions.

This analysis helped identify which features most influenced the prediction of instructor effectiveness.

Key influential features include:

* Learning Score
* Completion Rate
* Engagement Score
* Feedback Quality
* Dropout Rate

---

## Interactive Dashboard

An interactive dashboard was developed using **Streamlit** to visualize key insights.

Dashboard features include:

* Dataset preview
* Instructor tier distribution
* Model accuracy
* Feature importance visualization

The dashboard allows users to explore instructor performance interactively.

---

## Technologies Used

Programming Language:

* Python

Libraries:

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* SHAP
* Streamlit

---

## Project Structure

project-folder
│
├── project.ipynb
├── app.py
├── requirements.txt
├── dataset.csv
└── README.md

---

## Key Insights

* Higher learner engagement significantly improves completion rates.
* Instructors with strong learning score improvements tend to achieve higher effectiveness scores.
* Dropout rate negatively impacts instructor performance.
* Feedback quality is an important predictor of instructor effectiveness.

---

## Limitations

* Course difficulty level is not included in the dataset.
* Student demographic information is not available.
* External factors affecting engagement are not captured.

---

## Future Improvements

Possible enhancements include:

* Incorporating student demographic features
* Tracking instructor performance over time
* Adding real-time analytics dashboards
* Deploying the model as a cloud-based service

---

## Author

Saloni Saini

Machine Learning and Data Science Project
