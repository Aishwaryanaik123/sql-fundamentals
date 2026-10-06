import asyncio
import os

from vanna import Agent, AgentConfig, User
from vanna.core.registry import ToolRegistry
from vanna.core.user import UserResolver, RequestContext
from vanna.integrations.openai import OpenAILlmService
from vanna.integrations.sqlite import SqliteRunner
from vanna.integrations.local.agent_memory import DemoAgentMemory
from vanna.tools import RunSqlTool


class SimpleUserResolver(UserResolver):

    async def resolve_user(self, request_context: RequestContext) -> User:
        return User(
            id="demo-user",
            username="demo",
            email="demo@example.com",
            group_memberships=["user"]
        )


async def main():

    # Check OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY is not set.")
        return

    # Database path
    database_path = os.path.abspath("sales.db")

    # OpenAI model
    model = os.getenv("OPENAI_MODEL", "gpt-5")

    print(f"Using model: {model}")
    print(f"Using database: {database_path}")

    # Create OpenAI service
    llm = OpenAILlmService(
        model=model
    )

    # Create tool registry
    tool_registry = ToolRegistry()

    # Connect SQLite database
    sqlite_runner = SqliteRunner(
        database_path=database_path
    )

    # Create SQL tool
    sql_tool = RunSqlTool(
        sql_runner=sqlite_runner
    )

    # Register SQL tool
    tool_registry.register_local_tool(
        sql_tool,
        access_groups=[]
    )

    # Create user resolver
    user_resolver = SimpleUserResolver()

    # Create agent memory
    agent_memory = DemoAgentMemory(
        max_items=1000
    )

    # Create Vanna Agent
    agent = Agent(
        llm_service=llm,
        tool_registry=tool_registry,
        user_resolver=user_resolver,
        agent_memory=agent_memory,
        config=AgentConfig(
            stream_responses=False,
            temperature=1.0
        )
    )

    # Create user
    user = User(
        id="demo-user",
        username="demo",
        email="demo@example.com",
        group_memberships=["user"]
    )

    # Create request context
    request_context = RequestContext(
        user=user
    )

    # Conversation
    conversation_id = "sales-analysis"

    # Test question
    question = "How many sales records are there?"

    print()
    print("Question:")
    print(question)
    print()
    print("Vanna response:")
    print("-" * 50)

    # Send question to Vanna
    async for component in agent.send_message(
        request_context,
        question,
        conversation_id=conversation_id
    ):

        if hasattr(component, "content") and component.content:
            print(component.content)

    print("-" * 50)


if __name__ == "__main__":
    asyncio.run(main())