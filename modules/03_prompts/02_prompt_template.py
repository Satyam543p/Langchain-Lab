from langchain.chat_models import init_chat_model  
from langchain_core.prompts import PromptTemplate              #importing chatpromptTemplate for making prompts
from dotenv import load_dotenv

load_dotenv()       
model=init_chat_model("nvidia/nemotron-3.5-lightning:free",model_provider="openrouter")

template=PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

prompt=template.invoke({"name":"satyam"})

print()
print("#-----PROMPT-----#")

print(prompt)    #output:text='Greet this person in 5 languages. The name of the person is satyam'
print()
print("-------AI response------")
print()
result=model.invoke(prompt)
print(result.content)