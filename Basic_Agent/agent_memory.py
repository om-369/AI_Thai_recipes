from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.embedder.openai import OpenAIEmbedder
from agno.embedder.huggingface import HuggingfaceCustomEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb,SearchType
from dotenv import load_dotenv
load_dotenv()
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

from huggingface_hub import InferenceClient

client = InferenceClient(token=os.getenv("HF_TOKEN"))


agent = Agent(
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    description="You are a thai cusine expert!",
    instructions=[
        "Search your knowledge base for Thai recipes.",
        "If the question is better suited for the web, search the web to fill in the gaps.",
        "Prefer the information in your knowledge base over the web results."
    ],
    knowledge=PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="recipes",
            search_type=SearchType.hybrid,
            embedder=HuggingfaceCustomEmbedder(id="sentence-transformers/all-MiniLM-L6-v2"),
        ),
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

#Comment out the knowledge base is loaded
if agent.knowledge is not None:
    agent.knowledge.load()
    
agent.print_response("How do I make chicken and galangal in coconut milk soup?", stream=True)
agent.print_response("What is the history of Thai curry?",stream=True)