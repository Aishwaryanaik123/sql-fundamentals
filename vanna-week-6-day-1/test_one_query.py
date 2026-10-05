import asyncio

from vanna.core.user import RequestContext, User
from vanna.core.tool import ToolContext

from vanna_setup import agent
from train_vanna import training_examples


async def train_and_add_schema():

    user = User(
        id="admin",
        email="admin@example.com",
        group_memberships=["admin"],
    )

    print("Training 5 examples...")

    # ---------------------------------------------
    # Train 5 question -> SQL examples
    # ---------------------------------------------
    for i, example in enumerate(training_examples, start=1):

        context = ToolContext(
            user=user,
            conversation_id="test-session",
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

    print("Training completed.")

    # ---------------------------------------------
    # Add actual database schema to memory
    # ---------------------------------------------
    schema_context = """
Database: analytics.duckdb

Table name:
sales

The ONLY table used for this project is:
sales

Columns:
- id INTEGER
- product VARCHAR
- category VARCHAR
- city VARCHAR
- sales DOUBLE
- quantity INTEGER
- customer_rating DOUBLE

Important database rule:
Use the table name "sales" exactly.
There is NO table named "sales_table".

Examples:
SELECT SUM(sales) FROM sales;
SELECT AVG(sales) FROM sales;
"""

    schema_context_tool = ToolContext(
        user=user,
        conversation_id="test-session",
        request_id="schema-1",
        agent_memory=agent.agent_memory,
    )

    agent.agent_memory.save_text_memory(
        content=schema_context,
        context=schema_context_tool,
    )

    print("Database schema added to Vanna memory.")


async def test_query():

    request_context = RequestContext()

    question = "What is the total sales?"

    print()
    print("Question:")
    print(question)
    print()
    print("Vanna response:")
    print()

    async for component in agent.send_message(
        request_context=request_context,
        message=question,
        conversation_id="test-session",
    ):

        print("=" * 70)
        print("Component type:", type(component).__name__)
        print(component)
        print("=" * 70)


async def main():

    await train_and_add_schema()
    await test_query()


if __name__ == "__main__":
    asyncio.run(main())