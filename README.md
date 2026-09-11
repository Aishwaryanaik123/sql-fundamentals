# Data Cleaning – Week 2 Day 4

## Project Overview

This project focuses on cleaning and preparing an Employee dataset for further data analysis. The dataset contains employee information such as education, joining year, city, payment tier, age, gender, experience, and employee attrition.

## Dataset

The dataset used in this project is `Employee.csv`.

The dataset contains 4,653 rows and 9 columns.

## Data Cleaning Tasks

The following data cleaning operations were performed:

1. Identified and quantified missing values using `isnull().sum()`.
2. Applied missing value imputation strategies including mean, median, mode, and forward-fill.
3. Detected numerical outliers using the IQR method.
4. Capped detected outliers using IQR limits.
5. Standardised inconsistent string values by removing extra whitespace and standardising text casing.
6. Created a data quality log to document the cleaning decisions.
7. Exported the cleaned dataset as `cleaned_employee.csv`.

## Files

* `Employee.csv` – Original employee dataset
* `data_cleaning.py` – Python data cleaning script
* `cleaned_employee.csv` – Cleaned dataset
* `data_quality_log.csv` – Data cleaning decisions and actions
* `README.md` – Project documentation

## Technologies Used

* Python
* Pandas
* NumPy
* PyCharm
* Git
* GitHub

## Output

The cleaned dataset is saved as:

`cleaned_employee.csv`

The data quality log is saved as:

`data_quality_log.csv`

## Learning Outcome

This task provided practical experience in handling missing values, detecting outliers, standardising categorical data, documenting data quality decisions, and preparing a dataset for further analysis.
