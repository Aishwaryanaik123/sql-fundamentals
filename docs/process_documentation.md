# Process Documentation

## Objective
Build and demonstrate a simple AI Data Analyst Platform that can analyse a CSV dataset through a web interface.

## Implementation process
1. **Requirement understanding:** Identified the main workflow: upload data, inspect it, analyse it, visualise it and ask questions.
2. **Dataset preparation:** Added a small sales dataset so the platform can be demonstrated immediately without a separate upload.
3. **Data ingestion:** Used Pandas `read_csv()` to load the uploaded or sample CSV.
4. **Data overview:** Calculated row count, column count, missing cells and duplicate rows.
5. **Data profiling:** Displayed column data types, missing-value counts and numerical descriptive statistics.
6. **Visualisation:** Used Plotly to create bar, line, scatter and histogram charts.
7. **Question answering:** Created a local question engine to recognise common requests such as total, average, maximum, minimum, most frequent category, missing values and duplicate rows.
8. **User interface:** Used Streamlit tabs to organise the preview, profile, charts and analyst question area.
9. **Testing:** Prepared a demo checklist and example questions for validation.
10. **Version control:** Prepared Git commands and a descriptive commit message for the Week 12 Day 5 branch.

## Tools and technologies
- Python — application logic
- Pandas — data loading and analysis
- Streamlit — interactive web application
- Plotly — interactive charts
- Git and GitHub — version control and submission

## Expected result
The application opens in a browser, loads the sample sales dataset, displays dataset statistics, allows chart creation, and returns answers to supported analytical questions. A user can also upload another CSV file.

## Testing notes
The demo should be tested with the included `data/sales_data.csv`. Verify that the preview, profile tables, charts and sample questions work before presenting. Test an additional CSV upload if time permits.

## Limitation
The current question engine is rule-based and runs locally. It does not use an external LLM or claim to understand every possible question. This keeps the demo reproducible and avoids requiring an API key.
