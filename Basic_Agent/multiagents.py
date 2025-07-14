from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools


import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")


web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    # model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools = [DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    # model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_info=True)],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True,
)


agent_team = Agent(
    team=[web_agent, finance_agent],
    model=OpenAIChat(id="gpt-4o"),
    # model=Groq(id="deepseek-r1-distill-llama-70b"),
    show_tool_calls=True,
    markdown=True,
)


agent_team.print_response("Analyze the market outlook and financial performance of AI semiconductor company NVIDIA And Tesla And sugggest whether I have to buy or not?.", stream=True)
agent_team.print_response("Analyze the market outlook and financial performance of IT company KPIT And WIPRO And sugggest whether I have to buy or not?.", stream=True)
