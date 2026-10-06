training_data = [
    {
        "question": "How many sales records are there?",
        "sql": "SELECT COUNT(*) FROM sales;"
    },
    {
        "question": "What is the total sales amount?",
        "sql": "SELECT SUM(quantity * price) FROM sales;"
    },
    {
        "question": "What is the average product price?",
        "sql": "SELECT AVG(price) FROM sales;"
    },
    {
        "question": "Which region has the most sales records?",
        "sql": "SELECT region, COUNT(*) AS sales_count FROM sales GROUP BY region ORDER BY sales_count DESC;"
    },
    {
        "question": "What is the total quantity sold?",
        "sql": "SELECT SUM(quantity) FROM sales;"
    }
]