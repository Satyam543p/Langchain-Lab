from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGroq(model_name="qwen/qwen3.8-27b",max_tokens=300)

prompt=PromptTemplate(
    template='You are very good professor of {topic}.So based on student query please give appropriate answer.',
    input_variables=['topic']
)

parser=StrOutputParser() # give output in string or text only

chain = prompt | model | parser

result=chain.invoke({'topic':'langchain'})
print(result)

#output:Hello! I am ready to assist you. As a professor specializing in **LangChain**, I am here to help you navigate the complexities of building LLM applications.

# Whether you are a beginner looking to understand the core concepts or an advanced developer optimizing production-ready pipelines, please feel free to ask your question.

# To help me give you the most precise and useful answer, you might want to include details such as:
# *   **Your specific goal** (e.g., building a RAG system, creating a chatbot, using Agents, etc.).
# *   **The version of LangChain** you are using (e.g., LangChain 0.1.x, 0.2.x, or the newer `langgraph` ecosystem).
# *   **The LLM provider** you are working with (OpenAI, Anthropic, Ollama, etc.).
# *   **Any error messages** or code snippets you are struggling with.

# **What is your first question?**