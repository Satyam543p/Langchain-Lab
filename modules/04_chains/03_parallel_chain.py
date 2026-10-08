from langchain_groq import ChatGroq
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel  #we use it to run to chain parallel

load_dotenv()

model1 = ChatGroq(model_name="qwen/qwen3.8-27b",max_tokens=300)

model2 = ChatOpenRouter(model_name='nvidia/nemotron-3.5-lightning:free',max_tokens=300)

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following topic \n {topic}',
    input_variables=['text']
)    

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {topic}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain



result = chain.invoke({'topic':"langchain"})

print(result)

chain.get_graph().print_ascii()
#           +---------------------------+            
#           | Parallel<notes,quiz>Input |            
#           +---------------------------+            
#                 ***             ***                
#               **                   **              
#             **                       **            
# +----------------+              +----------------+ 
# | PromptTemplate |              | PromptTemplate | 
# +----------------+              +----------------+ 
#           *                             *          
#           *                             *          
#           *                             *          
#     +----------+                +----------------+ 
#     | ChatGroq |                | ChatOpenRouter | 
#     +----------+                +----------------+ 
#           *                             *          
#           *                             *          
#           *                             *          
# +-----------------+            +-----------------+ 
# | StrOutputParser |            | StrOutputParser | 
# +-----------------+            +-----------------+ 
#                 ***             ***                
#                    **         **                   
#                      **     **                     
#           +----------------------------+           
#           | Parallel<notes,quiz>Output |           
#           +----------------------------+           
#                          *                         
#                          *                         
#                          *                         
#                 +----------------+                 
#                 | PromptTemplate |                 
#                 +----------------+                 
#                          *                         
#                          *                         
#                          *                         
#                    +----------+                    
#                    | ChatGroq |                    
#                    +----------+                    
#                          *                         
#                          *                         
#                          *                         
#                 +-----------------+                
#                 | StrOutputParser |                
#                 +-----------------+                
#                          *                         
#                          *                         
#                          *                         
#             +-----------------------+              
#             | StrOutputParserOutput |              
#             +-----------------------+ 