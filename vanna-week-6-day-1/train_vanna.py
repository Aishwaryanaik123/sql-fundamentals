import asyncio

from vanna.core.tool import ToolContext
from vanna.core.user import User
from vanna.capabilities.agent_memory import ToolMemory

from vanna_setup import agent


# --------------------------------------------------
# 5 training question -> SQL examples
# --------------------------------------------------

training_examples = [
    ToolMemory(
        question="What is the total sales?",
        tool_name="run_sql",
        args={
            "sql": """
SELECT SUM(sales) AS total_sales
FROM sales;
"""
        },
    ),

    ToolMemory(
        question="What is the average sales?",
        tool_name="run_sql",
        args={
            "sql": """
SELECT AVG(sales) AS average_sales
FROM sales;
"""
        },
    ),

    ToolMemory(
        question="Which city has the highest sales?",
        tool_name="run_sql",
        args={
            "sql": """
SELECT city, SUM(sales) AS total_sales
FROM sales
GROUP BY city
ORDER BY total_sales DESC
LIMIT 1;
"""
        },
    ),

    ToolMemory(
        question="How many products are in each category?",
        tool_name="run_sql",
        args={
            "sql": """
SELECT category, COUNT(*) AS product_count
FROM sales
GROUP BY category
ORDER BY product_count DESC;
"""
        },
    ),

    ToolMemory(
        question="What is the average customer rating by category?",
        tool_name="run_sql",
        args={
            "sql": """
SELECT category, AVG(customer_rating) AS average_rating
FROM sales
GROUP BY category
ORDER BY average_rating DESC;
"""
        },
    ),
]


# --------------------------------------------------
# Train Vanna
# --------------------------------------------------

async def train():

    user = User(
        id="admin",
        email="admin@example.com",
        group_memberships=["admin"],
    )

    print()
    print("Starting Vanna training...")
    print()

    for i, example in enumerate(training_examples, start=1):

        context = ToolContext(
            user=user,
            conversation_id="training-session",
            request_id=f"training-{i}",
            agent_memory=agent.agent_memory,
        )

        await agent.agent_memory.save_tool_usage(
            question=example.question,
            tool_name=example.tool_name,
            args=example.args,
            context=context,
            success=True,
        )

        print(f"Training example {i}/5 added:")
        print(f"Question: {example.question}")
        print("SQL:")
        print(example.args["sql"].strip())
        print("-" * 60)

    print()
    print("Vanna training completed successfully.")
    print("Total training examples: 5")


# --------------------------------------------------
# Run
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(train())