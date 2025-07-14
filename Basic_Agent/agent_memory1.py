import streamlit as st
from agno.agent import Agent
from agno.models.groq import Groq
from agno.embedder.huggingface import HuggingfaceCustomEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

# Set environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")

client = InferenceClient(token=os.getenv("HF_TOKEN"))

# Initialize the agent
@st.cache_resource
def init_agent():
    return Agent(
        model=Groq(id="deepseek-r1-distill-llama-70b"),
        description="You are a Thai cuisine expert!",
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

# UI starts
st.set_page_config(page_title="Thai Recipe Agent", page_icon="🥘")

st.title("🥘 Thai Recipe Assistant")
st.markdown("Ask me anything about Thai cuisine, ingredients, or recipes!")

agent = init_agent()

# Load KB if not done already
if agent.knowledge is not None:
    with st.spinner("Loading knowledge base..."):
        agent.knowledge.load()

# User input
query = st.text_input("Enter your question:", placeholder="e.g., How do I make Thai green curry?")

if st.button("Ask"):
    if query:
        with st.spinner("Thinking..."):
            response = agent.run(query)
            st.markdown(response.content, unsafe_allow_html=True)