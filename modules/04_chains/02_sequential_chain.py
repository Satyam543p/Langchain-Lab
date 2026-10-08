from langchain.chat_models import init_chat_model  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser  #For makke Output in srting 
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)      
model=init_chat_model("qwen/qwen3.8-27b",model_provider="groq",max_tokens=500)

parser=StrOutputParser()    #we will discuss about it in strucutred output module


chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'Unemployment in India'})

print(result)

chain.get_graph().print_ascii()