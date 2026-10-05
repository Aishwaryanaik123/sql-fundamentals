from vanna import Agent
from vanna.core.registry import ToolRegistry
from vanna.core.user import UserResolver, User, RequestContext
from vanna.tools import RunSqlTool
from vanna.tools.agent_memory import (
    SaveQuestionToolArgsTool,
    SearchSavedCorrectToolUsesTool,
    SaveTextMemoryTool
)
from vanna.integrations.ollama import OllamaLlmService
from vanna.integrations.duckdb import DuckDBRunner
from vanna.integrations.local.agent_memory import DemoAgentMemory


# --------------------------------------------------
# 1. Connect Vanna to Ollama
# --------------------------------------------------

llm = OllamaLlmService(
    model="llama3.2:3b",
    host="http://localhost:11434"
)


# --------------------------------------------------
# 2. Connect Vanna to DuckDB
# --------------------------------------------------

db_runner = DuckDBRunner(
    database_path="./analytics.duckdb"
)

db_tool = RunSqlTool(
    sql_runner=db_runner
)


# --------------------------------------------------
# 3. Configure agent memory
# --------------------------------------------------

agent_memory = DemoAgentMemory(
    max_items=1000
)


# --------------------------------------------------
# 4. User authentication
# --------------------------------------------------

class SimpleUserResolver(UserResolver):

    async def resolve_user(
        self,
        request_context: RequestContext
    ) -> User:

        return User(
            id="intern-user",
            email="intern@example.com",
            group_memberships=["admin", "user"]
        )


user_resolver = SimpleUserResolver()


# --------------------------------------------------
# 5. Create tool registry
# --------------------------------------------------

tools = ToolRegistry()

tools.register_local_tool(
    db_tool,
    access_groups=["admin", "user"]
)

tools.register_local_tool(
    SaveQuestionToolArgsTool(),
    access_groups=["admin"]
)

tools.register_local_tool(
    SearchSavedCorrectToolUsesTool(),
    access_groups=["admin", "user"]
)

tools.register_local_tool(
    SaveTextMemoryTool(),
    access_groups=["admin", "user"]
)


# --------------------------------------------------
# 6. Create Vanna Agent
# --------------------------------------------------

agent = Agent(
    llm_service=llm,
    tool_registry=tools,
    user_resolver=user_resolver,
    agent_memory=agent_memory
)


print("Vanna agent created successfully.")
print("LLM: Ollama - llama3.2:3b")
print("Database: DuckDB - analytics.duckdb")
print("Memory: DemoAgentMemory")
print("Vanna setup completed successfully.")