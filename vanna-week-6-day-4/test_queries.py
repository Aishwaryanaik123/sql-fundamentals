# 10 natural-language queries for manual SQL verification

TEST_QUERIES = [
    "How many sales records are there?",
    "What is the total sales revenue?",
    "What is the average unit price?",
    "How many units were sold in Bangalore?",
    "What is the revenue by product?",
    "Which region generated the highest revenue?",
    "How many products are in the Electronics category?",
    "What is the total quantity sold?",
    "What is the revenue from Furniture?",
    "Show sales revenue by region.",
]

if __name__ == "__main__":
    for i, query in enumerate(TEST_QUERIES, start=1):
        print(f"{i}. {query}")
