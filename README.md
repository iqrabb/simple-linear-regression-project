Machine Learning - Simple Linear Regression Project
Project Overview

This project demonstrates the implementation of a Simple Linear Regression model using Machine Learning techniques in Python. The objective is to analyze the relationship between students' study hours and their exam scores and build a predictive model that can estimate exam performance based on study time.

Simple Linear Regression is one of the fundamental supervised learning algorithms used for predicting continuous numerical values. In this project, the model learns the relationship between study hours (independent variable) and exam scores (dependent variable) from historical data and generates predictions for new inputs.

Problem Statement

Students often want to understand how study time affects academic performance. This project aims to predict exam scores based on the number of hours a student studies.

Input Variable (X):

Study Hours

Output Variable (Y):

Exam Score
Dataset Information

The dataset contains two features:

Feature	Description
Study Hours	Number of hours spent studying
Exam Score	Score obtained in the exam

The dataset is small, clean, and suitable for demonstrating the concepts of Simple Linear Regression.

Technologies and Libraries Used
Python
Google Colab
Pandas
NumPy
Matplotlib
Scikit-Learn
Project Workflow
1. Data Loading

The dataset was loaded into a Pandas DataFrame for analysis and preprocessing.

2. Data Visualization

A scatter plot was created to visualize the relationship between study hours and exam scores.

3. Data Splitting

The dataset was divided into training and testing sets using train_test_split().

4. Model Training

A Simple Linear Regression model was trained using Scikit-Learn's Linear Regression algorithm.

5. Prediction

The trained model was used to predict exam scores based on study hours.

6. Model Evaluation

The model performance was evaluated using the R² Score metric.

Model Performance

R² Score: 97.71%

The high R² value indicates that the model successfully captures the relationship between study hours and exam scores and provides highly accurate predictions.

Regression Equation

Exam Score = 7.1567 × Study Hours + 26.3438

Interpretation
The coefficient (7.1567) indicates that for every additional hour studied, the predicted exam score increases by approximately 7.16 marks.
The intercept (26.3438) represents the estimated score when study hours are zero.
Sample Prediction

Input:

Study Hours = 5

Predicted Output:

Exam Score = 62.13
Learning Outcomes

Through this project, the following concepts were learned:

Machine Learning Fundamentals
Supervised Learning
Simple Linear Regression
Data Visualization
Model Training and Testing
Prediction and Evaluation

Author

Iqra Bibi
