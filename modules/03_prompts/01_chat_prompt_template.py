from langchain.chat_models import init_chat_model  
from langchain_core.prompts import ChatPromptTemplate              #importing chatpromptTemplate for making prompts
from dotenv import load_dotenv

load_dotenv()       
model=init_chat_model("nvidia/nemotron-3.5-lightning:free",model_provider="openrouter")

template=ChatPromptTemplate(
   [('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')]   #Making prompt template
) 

prompt=template.invoke({"domain":"CODING","topic":"Langchain"})   #Making prompt

print()
print("#-----PROMPT-----#")

print(prompt)    #output:('system', 'You are a helpful {domain} expert'),('human', 'Explain in simple terms, what is {topic}')

print()
print("-------AI response------")
print()
result=model.invoke(prompt)
print(result.content)