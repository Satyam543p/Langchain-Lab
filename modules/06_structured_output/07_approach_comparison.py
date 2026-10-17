from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()


#Here we will Both with_structured_output and parser at once to see difference


class Parser(BaseModel):
    text:str

model=ChatGroq(model_name="qwen/qwen3.8-27b",max_tokens=200)


model1=ChatGroq(model_name="qwen/qwen3.8-27b",max_tokens=200).with_structured_output(Parser)


prompt=PromptTemplate(
    template='You are very good professor of {topic}.So based on student query please give appropriate answer.',
    input_variables=['topic']
)

parser=PydanticOutputParser(pydantic_object=Parser)

prompt1=PromptTemplate(
    template='You are very good professor of {topic}.So based on student query please give appropriate answer.in this format:{format}',
    input_variables=['topic'],
    partial_variables={"format":parser.get_format_instructions()}
)

 # give output in string or text only

chain = prompt1 | model | parser

result=chain.invoke({'topic':'langchain'})
print(result)
print(type(result))  

print()
print("------with structured output------")

chain1=prompt | model1
result1=chain1.invoke({'topic':'langchain'})
print(result1)
print(type(result1))

#text='Hello! I am ready to assist you as a LangChain professor. Please provide your specific query regarding LangChain, and I will give you an appropriate answer.'
# <class '__main__.Parser'>

# ------with structured output------
# text="Hello! I'm ready to help you with LangChain. Please share your question or query about LangChain, and I'll provide a detailed and clear answer as your professor would."
# <class '__main__.Parser'>