from agents import Runner, trace
from deep_agents.query_agent import QueryResponse
from deep_agents.query_agent import query_agent

class ResearchCoordinator:
    def __init__(self, query: str):
        self.query = query

    async def research(self) -> str:
        with trace("Deep Reseach Workflow")
        
    async def generate_queries() -> QueryResponse:
        result = await Runner.run(query_agent, input=self.query)

    