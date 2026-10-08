from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from langchain_core.runnables import RunnableBranch,RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGroq(model_name="qwen/qwen3.8-27b",max_tokens=300)

class Text(BaseModel):
    text:str
    sentiment:Literal['positive','negative']=Field(description="Give the sentiment of the text")

parser=StrOutputParser()

parser1 = PydanticOutputParser(pydantic_object=Text)


prompt1 = PromptTemplate(
    template='Read this text and tell its sentiment positive or negative as that text as well . \n {text} \n {format_instruction}',
    input_variables=['text'],
    partial_variables={'format_instruction':parser1.get_format_instructions()}
)    

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {text}',
    input_variables=['text']
)

classifier_chain=prompt1 | model | parser1


#Conditional chains

conditional_chain=RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain=classifier_chain | conditional_chain

result=chain.invoke({"text":"Lovely"})

print(result)

chain.get_graph().print_ascii()

#Output

# Thank you! I'm glad you like it. Is there anything else I can help you with today?
#     +-------------+      
#     | PromptInput |      
#     +-------------+      
#             *            
#             *            
#             *            
#    +----------------+    
#    | PromptTemplate |    
#    +----------------+    
#             *            
#             *            
#             *            
#       +----------+       
#       | ChatGroq |       
#       +----------+       
#             *            
#             *            
#             *            
# +----------------------+ 
# | PydanticOutputParser | 
# +----------------------+ 
#             *            
#             *            
#             *            
#        +--------+        
#        | Branch |        
#        +--------+        
#             *            
#             *            
#             *            
#     +--------------+     
#     | BranchOutput |     
#     +--------------+  