import pandas as pd
import logging

# Configure error logging
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    # Load Indian COVID-19 dataset
    df = pd.read_csv("data/indian_covid19.csv")

    # Remove aggregate Total row
    df = df[df["State"] != "Total"].copy()

    print("Dataset loaded successfully")
    print("Shape:", df.shape)

    queries = {
        1: "Which state has the highest confirmed cases?",
        2: "Which state has the highest number of recovered cases?",
        3: "Which state has the highest number of deaths?",
        4: "Which state has the highest number of active cases?",
        5: "What is the total number of confirmed cases?",
        6: "What is the total number of recovered cases?",
        7: "What is the total number of deaths?",
        8: "What is the average number of confirmed cases per state?",
        9: "Which state has the highest daily increase in confirmed cases?",
        10: "Which state has the lowest number of active cases?"
    }

    print("\n10 Natural Language Queries")
    print("=" * 50)

    for number, question in queries.items():
        print(f"{number}. {question}")

    print("\nAnswers using Pandas")
    print("=" * 50)

    print("1.", df.loc[df["Confirmed"].idxmax(), "State"])
    print("2.", df.loc[df["Recovered"].idxmax(), "State"])
    print("3.", df.loc[df["Deaths"].idxmax(), "State"])
    print("4.", df.loc[df["Active"].idxmax(), "State"])
    print("5.", df["Confirmed"].sum())
    print("6.", df["Recovered"].sum())
    print("7.", df["Deaths"].sum())
    print("8.", df["Confirmed"].mean())
    print("9.", df.loc[df["Delta_Confirmed"].idxmax(), "State"])
    print("10.", df.loc[df["Active"].idxmin(), "State"])

except FileNotFoundError as e:
    logging.error("Dataset file not found: %s", e)
    print("Error: Dataset file not found.")

except KeyError as e:
    logging.error("Required column missing: %s", e)
    print("Error: Required column is missing.")

except Exception as e:
    logging.exception("Unexpected error occurred: %s", e)
    print("Error:", e)