# Full Demo Script

1. Introduce the project: "This is my 3M capstone AI Data Analyst Platform. It helps users explore a dataset, understand data quality, create visualisations and ask analytical questions."
2. Start the application using `py -m streamlit run app.py`.
3. Show the sample dataset loaded by default.
4. In **Data preview**, scroll through the records and demonstrate the CSV download.
5. In **Data profile**, explain the column types, missing-value counts and numerical summary.
6. In **Visualisations**, select Category as the X-axis and Sales as the numeric field. Show the bar chart, then demonstrate another chart type.
7. In **Ask the analyst**, ask "What is the total Sales?" and "What is the average Profit?".
8. Ask "Which Category is most common?" and "Show missing values.".
9. Upload another CSV using the sidebar and explain that the same workflow can be used with a user's own dataset.
10. Conclude: "The platform brings data upload, profiling, visualisation and question answering into one simple interface."

**Presentation tip:** Explain that this version uses a local rule-based question engine. An LLM/API integration can be added as a future enhancement.
