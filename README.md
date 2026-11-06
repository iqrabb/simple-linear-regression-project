# Student Exam Score Prediction — Simple Linear Regression

A beginner-friendly machine-learning notebook demonstrating how **study hours** can be used as a single feature to estimate **exam scores** with Scikit-learn's Linear Regression.

This project is an educational exercise in supervised learning, exploratory analysis, visualization, model fitting, and prediction.

## Project objective

Explore the relationship between the number of hours a student studies and their exam score, then fit a simple linear regression model to that relationship.

- **Feature (X):** Study Hours
- **Target (y):** Exam Score
- **Problem type:** Supervised regression
- **Algorithm:** Scikit-learn `LinearRegression`

## Workflow

1. Load the student study-hours dataset into a Pandas DataFrame.
2. Inspect the data and select the feature and target columns.
3. Visualize study hours against exam scores with a scatter plot.
4. Fit a linear regression model.
5. Generate predictions and visualize the fitted regression line.
6. Review the model's coefficient, intercept, and R² score.

> **Evaluation note:** The current notebook fits and evaluates the model on the same 29 observations; it does not implement a train/test split. Therefore, the reported R² value (approximately 97.71%) is a training-set result, not an estimate of performance on unseen data. It should not be presented as a validated test score.

## Regression equation

The notebook reports the fitted equation:

```text
Exam Score = 7.1567 × Study Hours + 26.3438
```

The slope describes the change in the model's estimated exam score for one additional study hour within the observed data range. The intercept is the model's estimated score at zero study hours; it should be interpreted cautiously if zero hours is outside the meaningful range of the dataset.

## Technology

- Python
- Google Colab / Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Run the notebook

1. Open `Machine_Learning_Linear_Regression.ipynb` in Google Colab or Jupyter.
2. Make the dataset available at the path expected by the notebook, or update the data-loading cell to point to your local CSV file.
3. Run the notebook cells from top to bottom.

**Data note:** The notebook currently references a Google Drive path (`/content/drive/MyDrive/student_exam_data_v1.csv`). The CSV is not included in this repository, so you must supply the file yourself or update the notebook's data-loading path.

## Repository contents

- `Machine_Learning_Linear_Regression.ipynb` — notebook containing the analysis and model implementation.
- `README.md` — project documentation.
- `LICENSE` — repository license.

## Limitations and next steps

- The dataset file is not currently committed, so the notebook is not fully reproducible from a fresh clone.
- The current R² score is measured on the training observations.
- The project uses only one feature and a small dataset.
- Add the dataset with its source/license, use a train/test split or cross-validation, and report held-out MAE, RMSE, and R².
- Include actual notebook output screenshots once the notebook has been run with the dataset available.

---

Created as a foundational practice project while learning machine learning and regression.
