from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.groq import Groq

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

agent = Agent(
    # model=OpenAIChat(id="gpt-4o"),
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    description= "You are a chat assistant please reply based on user queries",
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
    )

# agent.print_response("tell me the recent sports news that you know",stream=True)
# Prompt the agent to fetch a breaking news story from New York
# agent.print_response("Tell me about a breaking news story from New York.", stream=True)
agent.print_response("What is the latest score of india vs australia test match",stream=True)