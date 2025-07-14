# 🍜 Thai Cuisine Expert Agent using AGNO

This project builds an intelligent agent that answers questions about Thai cuisine. It leverages Retrieval-Augmented Generation (RAG) with a knowledge base of Thai recipes and uses Groq's LLM, Hugging Face embeddings, DuckDuckGo search, and LanceDB vector storage.

## 🚀 Features

- **LLM Backend**: `deepseek-r1-distill-llama-70b` (via Groq)
- **RAG Setup**: Embeds and indexes PDF recipes using Hugging Face & LanceDB
- **Tools**: DuckDuckGo for web search fallback
- **Streaming Responses**: Supports real-time output from the model
- **Simple Frontend**: Streamlit interface (optional)

---

## 🗂️ Project Structure

---

Basic_Agent/
├── agent_memory.py # Main script: CLI version
├── agent_memory1.py # Streamlit frontend
├── tmp/lancedb/ # Vector DB storage
├── .env # API keys
└── README.md

---

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/om-369/AI_Thai_recipes
cd Basic_Agent
```

# Optional but recommended

python -m venv agno
.\agno\Scripts\activate

---

pip install -r requirements.txt

---

```bash
pip install agno streamlit python-dotenv huggingface_hub

```

```bash

python agent_memory.py

```

streamlit run agent_memory1.py

```
---

📚 Knowledge Base
Source: ThaiRecipes.pdf

Embedded with: sentence-transformers/all-MiniLM-L6-v2

Stored in: tmp/lancedb/recipes.lance


---

✨ Example Prompts
"How do I make chicken and galangal in coconut milk soup?"

"What is the history of Thai curry?"

"What are the ingredients for tom yum goong?"

---

🧠 Agent Architecture
text
Copy
Edit
User Query
   ↓
[Knowledge Base] ← PDF → LanceDB ← HuggingFace Embedder
   ↓
[Agent (Groq LLM)]
   ↓
DuckDuckGo Tool (if needed)
   ↓
Final Answer

---
🧪 TODO / Ideas
Add support for OpenAI model switching

Allow local PDF upload via Streamlit

Add chat history and export

Deploy with Docker or Hugging Face Spaces


---

🙌 Credits
AGNO

Groq

HuggingFace

LanceDB

Thai recipes courtesy of phi-public.s3.amazonaws.com

---
# AI_Thai_recipes
```
