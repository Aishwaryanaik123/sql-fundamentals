import asyncio

from vanna.integrations import SqliteRunner
from vanna.capabilities.sql_runner.models import RunSqlToolArgs


async def main():
    # Connect to SQLite database
    runner = SqliteRunner("sales.db")

    print("SQLite connection created successfully!")

    # Create SQL arguments
    args = RunSqlToolArgs(
        sql="SELECT * FROM sales"
    )

    # Execute SQL
    result = await runner.run_sql(args, None)

    print("\nSales data:")
    print(result)


asyncio.run(main())