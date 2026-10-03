\# PandasAI - Week 5 Day 1



\## Objective



The objective of this practical is to explore PandasAI for natural-language data analysis using an Indian COVID-19 dataset.



\## Tasks Completed



1\. Installed and configured PandasAI.

2\. Loaded an Indian COVID-19 CSV dataset.

3\. Created 10 natural-language data analysis questions.

4\. Verified the questions using manual Pandas operations.

5\. Compared PandasAI and manual Pandas for 3 questions.

6\. Added error handling for failed queries.

7\. Added error logging using Python logging.

8\. Created a requirements.txt file.



\## Dataset



The dataset contains state-wise COVID-19 information for India.



\### Dataset columns



\- State

\- Confirmed

\- Recovered

\- Deaths

\- Active

\- Last\_Updated\_Time

\- Migrated\_Other

\- State\_code

\- Delta\_Confirmed

\- Delta\_Recovered

\- Delta\_Deaths

\- State\_Notes



The aggregate `Total` row was removed before performing state-level analysis.



\## 10 Natural Language Queries



1\. Which state has the highest confirmed cases?

2\. Which state has the highest number of recovered cases?

3\. Which state has the highest number of deaths?

4\. Which state has the highest number of active cases?

5\. What is the total number of confirmed cases?

6\. What is the total number of recovered cases?

7\. What is the total number of deaths?

8\. What is the average number of confirmed cases per state?

9\. Which state has the highest daily increase in confirmed cases?

10\. Which state has the lowest number of active cases?



\## Manual Pandas Results



| Question | Result |

|---|---|

| Highest confirmed cases | Maharashtra |

| Highest recovered cases | Maharashtra |

| Highest deaths | Maharashtra |

| Highest active cases | Kerala |

| Total confirmed cases | 34,285,612 |

| Total recovered cases | 33,661,339 |

| Total deaths | 458,470 |

| Average confirmed cases | 926,638.16 |

| Highest daily increase | Andaman and Nicobar Islands |

| Lowest active cases | Lakshadweep |



\## PandasAI vs Manual Pandas



Three questions were selected for comparison:



1\. Which state has the highest confirmed cases?

2\. Which state has the highest number of deaths?

3\. Which state has the highest number of active cases?



Manual Pandas was used to verify the expected results.



PandasAI natural-language execution could not be completed because the configured OpenAI API account had no remaining API credits. Therefore, PandasAI results were not fabricated and are marked as pending API access.



\## Error Handling



The project uses Python's `logging` module to record errors in `error.log`.



The program handles:



\- Missing dataset files

\- Missing required columns

\- Unexpected exceptions



\## Files



\- `pandasai\_analysis.py` - Main analysis program

\- `comparison.py` - PandasAI vs Manual Pandas comparison

\- `data/indian\_covid19.csv` - Indian COVID-19 dataset

\- `error.log` - Error log

\- `requirements.txt` - Python dependencies

\- `README.md` - Project documentation



\## Tools Used



Python, PandasAI, Pandas, OpenAI, LiteLLM, Matplotlib, Git, GitHub, PowerShell, VS Code/Notepad

