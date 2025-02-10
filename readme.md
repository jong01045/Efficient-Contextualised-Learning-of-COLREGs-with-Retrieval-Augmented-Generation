# Self-Reflective Agent

Welcome to the **Self-Reflective Agent** project! This guide will walk you through setting up the environment, configuring API keys, and running the agent for evaluation. Please ensure you meet the prerequisites and follow the steps below carefully.

**Also if you need a detailed explanation of the project structure and each component, contact me through the email (Bottom of README file)**

---

## Requirements

- **Python Version**: 3.12
- **Hardware**: Minimum 6GB VRAM (required for embedding models)
- **Dependencies**: Listed in `requirement.txt`

---

## Setup Instructions

### 1. Create a Virtual Environment

```bash
python3.12 -m venv self_reflective_env
```

### 2. Activate the Virtual Environment

- **Windows**:
  ```bash
  self_reflective_env\Scripts\activate
  ```
- **MacOS/Linux**:
  ```bash
  source self_reflective_env/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirement.txt
```

### 4. Configure API Keys

Create an `.env` file in the root directory and populate it with the following keys. Replace the placeholders `()` with your actual API keys.

```env
# LangChain Configuration
LANGCHAIN_TRACING_V2 = "true"
LANGCHAIN_API_KEY = "()"
LANGCHAIN_PROJECT = "()"

# API Keys
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
```

### 5. Open the Jupyter Notebook

Launch Jupyter Notebook and open the file `Self_reflective_agent.ipynb`:

```bash
jupyter notebook Self_reflective_agent.ipynb
```

### 6. Run the Notebook

Execute the notebook sections sequentially until the section titled **Final RAG Model Output**.

---

## Evaluation Results

Evaluation results for multiple questions are pre-stored in the `Eval_results` folder in JSON format. You can review these files without rerunning the model.

---

## Notes

- Ensure your system has at least **6GB VRAM** to handle the embedding model efficiently.
- Double-check your `.env` file for accurate API key configuration.
- If you encounter issues, verify your Python version and dependency installations.

---

### Contact

For further assistance, please reach out via email or open an issue in the repository.
jungho.career@gmail.com

---

Happy experimenting! 🚀

