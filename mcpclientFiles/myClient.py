from langchain_mcp_adapters.client import MultiServerMCPClient
from mcpConfig import connections
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import os

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

import asyncio

async def main():
    client = MultiServerMCPClient(connections=connections)

    tools = await client.get_tools()

    model = ChatGroq(model="deepseek-r1-distill-llama-70b")

    agent = create_react_agent(
        model,
        tools,
    )

    math_response = await agent.ainvoke(
    {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )

    print("Math response:", math_response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())