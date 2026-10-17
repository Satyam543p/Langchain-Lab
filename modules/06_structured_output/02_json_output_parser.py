from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

model=ChatGroq(model_name="qwen/qwen3.8-27b",max_tokens=300)

parser = JsonOutputParser()  #output in json

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)

# output:{'facts': ['Black holes are regions in space where gravity is so strong that nothing, not even light, can escape once it crosses the event horizon.', 
#                   'The mass of a black hole is concentrated at its center in a point of infinite density called a singularity.', 
#                   'Black holes can be stellar-mass, formed from the collapse of massive stars, or supermassive, found at the centers of most large galaxies.', 
#                   'Time dilation occurs near black holes, meaning time passes more slowly for an object close to the event horizon compared to a distant observer.', 
#                   "While black holes were first predicted by Einstein's theory of general relativity, the first direct image of a black hole's shadow was captured by the Event Horizon Telescope in 2019."]}