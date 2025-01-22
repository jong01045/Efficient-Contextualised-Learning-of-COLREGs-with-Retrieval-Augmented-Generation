1. First Create a virtual environment with python 3.12

2. Activate the virtual environment.

3. pip install -r requirement.txt

4. Create an .env file containing corresponding API Keys for a smooth run
    Anything () needs to be filled with your own Key
LANGCHAIN_TRACING_V2 = "true"
LANGCHAIN_API_KEY = "()"
LANGCHAIN_PROJECT = "()"
TAVILY_API_KEY = "()"
GROQ_API_KEY = "()"
OPENAI_API_KEY = "()" 
HUGGINGFACEHUB_API_TOKEN = "()"

UPSTAGE_API_KEY = "()"
AI21_API_KEY = "()"
JINA_API_KEY = "()"
VOYAGE_API_KEY = "()" 
COHERE_API_KEY = "()"
ANTHROPIC_API_KEY = "()"
LLAMA_CLOUD_API_KEY = "()"
PINECONE_API_KEY = "()"

5. Open the Jupyter notebook "Self_reflective_agent.ipynb"

6. Run until the section "Final RAG model output"


However the results for multiple questions are already stored in the Eval_results folder in a format of JSON

In order to run this agent, you need at least 6GB of VRAM (Because of the embedding model)
