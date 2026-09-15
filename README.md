# Week 2 Day 6 – Data Governance, Data Quality & Great Expectations

## Project Overview

This project focuses on data governance, data quality validation, data contracts, DAMA data quality dimensions, and PII classification using the Employee dataset.

The dataset was validated using Great Expectations, and intentional data quality errors were introduced to verify that the validation rules correctly detect invalid data.

## Dataset

**Dataset:** Employee.csv

**Rows:** 4,653

**Columns:** 9

### Columns

* Education
* JoiningYear
* City
* PaymentTier
* Age
* Gender
* EverBenched
* ExperienceInCurrentDomain
* LeaveOrNot

## Tasks Completed

### 1. DAMA Data Quality Assessment

The Employee dataset was evaluated using the six DAMA data quality dimensions:

* Accuracy
* Completeness
* Consistency
* Timeliness
* Validity
* Uniqueness

The dataset contains no missing values, while 1,889 duplicate rows were identified and documented for review.

### 2. Great Expectations Validation

Great Expectations was used to create and execute a suite of 8 data quality expectations.

The expectations validate:

1. Education is not null
2. JoiningYear is within the valid range
3. City contains valid values
4. PaymentTier is between 1 and 3
5. Age is between 18 and 60
6. Gender contains valid values
7. ExperienceInCurrentDomain is within the valid range
8. LeaveOrNot contains valid values

### 3. Intentional Data Quality Errors

Three errors were intentionally introduced into `Employee_quality_test.csv`:

* PaymentTier changed to an invalid value of 5
* Age changed to an invalid value of 150
* Gender changed to an invalid value of "Unknown"

Great Expectations successfully detected all three errors.

### 4. Data Contract

A YAML data contract was created to define:

* Data producer
* Data consumer
* Dataset schema
* Data types
* Valid ranges
* Allowed categorical values
* Quality rules
* Validation requirements
* Privacy and data protection recommendations

The producer is the data analyst and the consumer is the BI dashboard.

### 5. PII Classification

The dataset was reviewed for personally identifiable and sensitive employee information.

No direct identifiers such as employee name, email address, phone number, or employee ID are present in the dataset.

Potentially sensitive attributes such as Age, Gender, and employment-related fields should be restricted or aggregated when used in dashboards.

### 6. Data Quality Scorecard

A one-page DAMA data quality scorecard was created using Python and documented the quality scores, identified issues, and improvement recommendations.

## Project Files

```text
great-expectations-week-2-day-6/
│
├── Employee.csv
├── Employee_quality_test.csv
├── check_dataset.py
├── create_validation.py
├── generate_report.py
├── data_contract.yml
├── data_quality_scorecard.py
├── data_quality_scorecard.docx
├── README.md
│
├── gx/
│   ├── great_expectations.yml
│   ├── expectations/
│   │   └── employee_data_quality_suite.json
│   └── plugins/
│
└── validation_report/
    ├── validation_report.html
    └── validation_results.json
```

## Validation Results

| Metric              | Result |
| ------------------- | -----: |
| Total Expectations  |      8 |
| Passed Expectations |      5 |
| Failed Expectations |      3 |
| Intentional Errors  |      3 |
| Errors Detected     |      3 |
| Missing Values      |      0 |
| Duplicate Rows      |  1,889 |

## Recommendations

* Investigate and remove or review duplicate records.
* Run Great Expectations validation before every BI dashboard refresh.
* Enforce valid ranges and allowed categorical values during data ingestion.
* Standardize categorical data before analysis.
* Restrict access to sensitive employee attributes.
* Use aggregation or masking when sensitive information is displayed in dashboards.

## Tools Used

* Python
* Pandas
* Great Expectations
* PyYAML
* Python-docx
* Git
* GitHub
* PyCharm

## Learning Outcome

This project provided practical experience in data governance, data quality assessment, automated validation, data contracts, privacy considerations, and preparing reliable datasets for BI dashboard consumption.
