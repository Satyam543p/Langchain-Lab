from langchain.chat_models import init_chat_model  
from langchain_core.prompts import ChatPromptTemplate              #importing chatpromptTemplate for making prompts
from dotenv import load_dotenv

print("1 - Starting")

load_dotenv()

print("2 - Creating model")
model = init_chat_model(
    "gemini-2.5-flash",
    model_provider="google_genai"
)

print("3 - Creating prompt")

template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert"),
    ("human", "Explain in simple terms, what is {topic}")
])

print("4 - Creating chain")

chain = template | model

print("5 - Invoking chain")

result = chain.invoke({
    "domain": "CODING",
    "topic": "Langchain"
})

print("6 - Got response")
print(result.content)