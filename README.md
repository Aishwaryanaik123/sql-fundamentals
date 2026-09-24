# Correlation & Regression Analysis – Week 4 Day 3

## Overview

This project focuses on understanding relationships between variables using correlation analysis and building a simple linear regression model using Python and scikit-learn.

## Practical Tasks

* Calculate Pearson correlation coefficient
* Calculate Spearman correlation coefficient
* Visualize correlations using a correlation heatmap
* Create a scatter matrix
* Build a simple linear regression model using scikit-learn
* Generate predictions using the regression model
* Evaluate the model using R², MAE, and RMSE
* Plot and analyze residuals
* Check basic linear regression assumptions

## Dataset

The analysis uses a dataset containing:

* **Advertising_Spend** – Independent variable
* **Sales** – Dependent variable

The dataset was created directly in the Jupyter Notebook for analysis and demonstration.

## Analysis Performed

### Correlation Analysis

Pearson and Spearman correlation coefficients were calculated to measure the relationship between Advertising Spend and Sales.

### Correlation Visualization

A correlation matrix and heatmap were created to visualize the strength and direction of relationships between variables.

A scatter matrix was also created to visualize relationships between the variables.

### Linear Regression

A simple linear regression model was developed using:

* Independent variable: Advertising Spend
* Dependent variable: Sales
* Training data: 80%
* Testing data: 20%

The model was implemented using `LinearRegression` from scikit-learn.

### Model Evaluation

The regression model was evaluated using:

* **R² Score** – Measures the proportion of variance explained by the model.
* **MAE** – Measures the average absolute prediction error.
* **RMSE** – Measures the square root of the average squared prediction error.

### Residual Analysis

Residuals were calculated and visualized using:

* Residual scatter plot
* Residual distribution plot

These visualizations were used to check basic regression assumptions.

## Deliverable

* `regression_analysis.ipynb`

## Tools & Technologies

Python, Jupyter Notebook, Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn.

## Git Branch

`feature/week-4-day-3`

## Commit

`feat: correlation-regression week-4-day-3 complete`
