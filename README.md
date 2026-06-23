# Machine Learning - Simple Linear Regression Project

## Project Overview

This project demonstrates the implementation of a Simple Linear Regression model using Machine Learning techniques in Python. The primary objective is to analyze the relationship between students' study hours and their exam scores and build a predictive model capable of estimating exam performance based on study time.

Simple Linear Regression is one of the most fundamental supervised Machine Learning algorithms used for predicting continuous numerical values. In this project, the model learns the relationship between study hours (independent variable) and exam scores (dependent variable) from historical data and uses that relationship to make predictions for new observations.

---

## Problem Statement

Academic performance is often influenced by the amount of time students dedicate to studying. This project aims to determine the relationship between study hours and exam scores and use Machine Learning to predict future exam results.

### Input Variable (X)

* Study Hours

### Output Variable (Y)

* Exam Score

---

## Dataset Information

The dataset contains two features:

| Feature     | Description                    |
| ----------- | ------------------------------ |
| Study Hours | Number of hours spent studying |
| Exam Score  | Score obtained in the exam     |

The dataset is clean, structured, and suitable for demonstrating the concepts of Simple Linear Regression.

---

## Technologies and Libraries Used

* Python
* Google Colab
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn

---

## Project Workflow

### 1. Data Loading

The dataset was imported and loaded into a Pandas DataFrame for analysis and processing.

### 2. Data Exploration

The dataset structure, shape, and basic information were examined to understand the available features.

### 3. Data Visualization

A scatter plot was created using Matplotlib to visualize the relationship between study hours and exam scores.

### 4. Data Splitting

The dataset was divided into training and testing sets using the `train_test_split()` function from Scikit-Learn.

### 5. Model Training

A Simple Linear Regression model was trained using Scikit-Learn's `LinearRegression()` algorithm.

### 6. Prediction

The trained model was used to predict exam scores based on study hours.

### 7. Model Evaluation

The performance of the model was evaluated using the R² Score metric.

---

## Model Performance

**R² Score:** 97.71%

The model achieved an R² Score of 97.71%, indicating a very strong relationship between study hours and exam scores. This means the model explains approximately 97.71% of the variation in exam scores.

---

## Regression Equation

```text
Exam Score = 7.1567 × Study Hours + 26.3438
```

### Interpretation

* The coefficient (7.1567) indicates that for every additional hour studied, the predicted exam score increases by approximately 7.16 marks.
* The intercept (26.3438) represents the estimated exam score when study hours are zero.

---

## Sample Prediction

### Input

* Study Hours = 5

### Predicted Output

* Exam Score = 62.13

This prediction demonstrates how the model can estimate exam performance based on study time.

---

## Data Visualization

The project includes:

* Scatter Plot for data visualization
* Regression Line for trend analysis
* Predicted vs Actual comparison

These visualizations help in understanding the relationship between study hours and exam scores.

---

## Learning Outcomes

Through this project, the following concepts were learned:

* Introduction to Machine Learning
* Supervised Learning Techniques
* Simple Linear Regression
* Data Preprocessing
* Data Visualization using Matplotlib
* Model Training and Testing
* Prediction and Evaluation
* Performance Measurement using R² Score

---

## Author

**Iqra Bibi**

