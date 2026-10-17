from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

model=ChatGroq(model_name="qwen/qwen3.8-27b",max_tokens=300)

class test(BaseModel):
    name:list[str]=Field(description='name of cars')
    brand:list[str]=Field(description='Name of brands')
    Max_speed:list[str]=Field(description="max Speed of cars in Km/Hr")

parser=PydanticOutputParser(pydantic_object=test)    # give output as exactly in our test class format



prompt=PromptTemplate(
    template='When i will give you any number n:{n} then suggest me numbers of distinct car equal to number n mentaining the sturture format as given :{format} ',
    input_variables=['n'],
    partial_variables={'format':parser.get_format_instructions()}

)



chain = prompt | model | parser

result=chain.invoke({'n':2})
print(result)  

#output: name=['Toyota Corolla', 'Honda Civic'] brand=['Toyota', 'Honda'] Max_speed=['240 km/h', '230 km/h']