\# Week 4 Day 5 – Capstone Analysis



\## Project Overview



This capstone project performs an end-to-end analysis of government fund utilization data. The analysis covers data cleaning, exploratory data analysis, data visualization, statistical analysis, and an interactive Power BI dashboard.



The project uses a dataset containing 1,000 government fund records across multiple states, departments, schemes, implementing agencies, and project statuses.



\## Business Question



How effectively are government funds being utilized across different states, departments, schemes, and implementing agencies, and what factors are associated with differences in fund utilization and beneficiary coverage?



\## Objectives



\* Analyze sanctioned, released, and utilized government funds.

\* Compare fund utilization across states, departments, and schemes.

\* Analyze physical achievement and beneficiary coverage.

\* Examine fund utilization across different project statuses.

\* Identify relationships between financial utilization and operational outcomes.

\* Build an interactive Power BI dashboard for performance monitoring.

\* Provide actionable recommendations based on the analysis.



\## Dataset



\*\*Dataset:\*\* `govt\_fund\_utilization.csv`



\*\*Rows:\*\* 1,000



\*\*Original columns:\*\* 21



The dataset contains information related to:



\* Financial Year

\* Date of Fund Release

\* State

\* District

\* Department

\* Scheme Name

\* Scheme Code

\* Fund Source

\* Implementing Agency

\* Sanctioned Amount

\* Fund Released

\* Fund Utilized

\* Utilization Percentage

\* Physical Targets and Achievements

\* Beneficiary Targets and Coverage

\* Project Status

\* Audit Remarks



Contact information was excluded from the analysis dataset.



\## Data Cleaning



The following data-cleaning steps were performed:



\* Removed contact information from the analysis.

\* Converted the fund release date into datetime format.

\* Handled missing numerical values using median imputation.

\* Replaced missing audit remarks with a descriptive placeholder.

\* Verified duplicate records.

\* Verified remaining missing values.

\* Created physical achievement and beneficiary coverage percentage metrics.



After cleaning:



\* \*\*Rows:\*\* 1,000

\* \*\*Analysis columns:\*\* 22

\* \*\*Duplicate rows:\*\* 0

\* \*\*Missing values:\*\* 0



\## Exploratory Data Analysis



The analysis examined:



\* Overall financial utilization

\* State-level utilization

\* Department-level utilization

\* Scheme-level utilization

\* Project status distribution

\* Beneficiary coverage

\* Physical achievement

\* Relationships between financial and operational indicators



\## Key Metrics



| Metric                    |           Result |

| ------------------------- | ---------------: |

| Total Sanctioned Amount   | 400,073.92 Lakhs |

| Total Fund Released       | 297,951.32 Lakhs |

| Total Fund Utilized       | 201,934.77 Lakhs |

| Overall Fund Utilization  |           67.77% |

| Physical Achievement Rate |           64.18% |

| Beneficiary Coverage Rate |           61.41% |

| Number of States          |               10 |

| Number of Schemes         |               11 |

| Number of Departments     |                5 |



\## Statistical Analysis



\### Pearson Correlation



Fund utilization showed a positive correlation with:



\* \*\*Physical Achievement:\*\* `r = 0.6284`, `p < 0.001`

\* \*\*Beneficiary Coverage:\*\* `r = 0.3865`, `p < 0.001`



These results indicate associations within the dataset and do not establish causation.



\### One-Way ANOVA



A one-way ANOVA was used to examine differences in fund utilization across project status groups.



\* \*\*F-statistic:\*\* 673.7816

\* \*\*p-value:\*\* < 0.001



The result indicates statistically significant differences in mean fund utilization across at least one of the project-status groups.



\## Visualizations



The project includes visualizations for:



\* Fund utilization by state

\* Sanctioned vs released vs utilized funds

\* Fund utilization by department

\* Fund utilization by scheme

\* Project status distribution

\* Fund utilization by project status

\* Fund utilization vs physical achievement

\* Fund utilization vs beneficiary coverage



\## Power BI Dashboard



The Power BI dashboard provides an interactive view of:



\* Total sanctioned funds

\* Total released funds

\* Total utilized funds

\* Fund utilization percentage

\* Physical achievement percentage

\* Beneficiary coverage percentage

\* State-level performance

\* Department-level performance

\* Scheme-level performance

\* Project status

\* Financial-year analysis



\### Dashboard Files



\* `Capstone\_Government\_Fund\_Utilization\_Dashboard.pbix`

\* `capstone\_dashboard.png`

\* `capstone\_dashboard\_data.csv`



\## Executive Summary



The `executive\_summary.md` file contains the major findings and three actionable recommendations based on the analysis.



\## Project Files



```text

capstone-analysis-week-4-day-5/

│

├── capstone\_analysis.ipynb

├── capstone\_dashboard\_data.csv

├── govt\_fund\_utilization.csv

├── Capstone\_Government\_Fund\_Utilization\_Dashboard.pbix

├── capstone\_dashboard.png

├── executive\_summary.md

└── README.md

```



\## Tools and Technologies



Python, Jupyter Notebook, Pandas, NumPy, Matplotlib, Seaborn, SciPy, Power BI, Git, and GitHub.



\## Conclusion



The capstone provides an end-to-end analytical workflow for examining government fund utilization and related operational outcomes. The combination of statistical analysis and an interactive Power BI dashboard provides a structured way to monitor financial utilization, physical achievement, beneficiary coverage, and project status.



