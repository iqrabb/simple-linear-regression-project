# Machine Learning - Simple Linear Regression Project

## Project Overview

This project demonstrates the implementation of a Simple Linear Regression model using Machine Learning techniques in Python.

## Problem Statement

Students often want to understand how study time affects academic performance.

### Input Variable (X)

- Study Hours

### Output Variable (Y)

- Exam Score

## Dataset Information

The dataset contains two features:

| Feature | Description |
|----------|-------------|
| Study Hours | Number of hours spent studying |
| Exam Score | Score obtained in the exam |

## Technologies and Libraries Used

- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn

## Project Workflow

### 1. Data Loading

The dataset was loaded into a Pandas DataFrame.

### 2. Data Visualization

A scatter plot was created to visualize the relationship between study hours and exam scores.

### 3. Data Splitting

The dataset was divided into training and testing sets.

### 4. Model Training

A Simple Linear Regression model was trained using Scikit-Learn.

### 5. Prediction

The trained model was used to predict exam scores.

### 6. Model Evaluation

The model performance was evaluated using the R² Score metric.

## Model Performance

**R² Score:** 97.71%

## Regression Equation

```text
Exam Score = 7.1567 × Study Hours + 26.3438


## Interpretation

- The coefficient (7.1567) indicates that for every additional hour studied, the predicted exam score increases by approximately 7.16 marks.
- The intercept (26.3438) represents the estimated exam score when study hours are zero.

## Sample Prediction

### Input

- Study Hours = 5

### Predicted Output

- Exam Score = 62.13

## Learning Outcomes

Through this project, the following concepts were learned:

- Machine Learning Fundamentals
- Supervised Learning
- Simple Linear Regression
- Data Visualization using Matplotlib
- Data Splitting using Train-Test Split
- Model Training and Testing
- Prediction and Model Evaluation

## Author

**Iqra Bibi**
