                 ##Demosatrating Model thorugh init_chat_model

from langchain.chat_models import init_chat_model        #importing chatmodels
from dotenv import load_dotenv

load_dotenv()                                            # loading our api key here though env file

model=init_chat_model("nvidia/nemotron-3-ultra-550b-a55b:free",model_provider="openrouter", temperature=1.4) #initiating our model
#if you wanna use openai,gemini,anthropic just change model name and model_provider inside it

message=input("Enter: ")                                 #prompting message 
result=model.invoke(message)                             #call on model with message
print(result.content)






                    ###Inspecting AI Message###

print("type:",type(result),"\n\n result: ",result.content ,"\n\n result Response Metadata: ", result.response_metadata, "\n\n result Usage Metadata: ",result.usage_metadata) 





                    ###checking what temperature do ###

#temperature=0(min)  vary(0-2)
#message1:your name  result:I am Nemotron 3 Ultra, a language model developed by NVIDIA.
#message2:your name  result:I am Nemotron 3 Ultra, a language model developed by NVIDIA.

#temperature=1.4 high
#message1:your name  result: My name is Nemotron 3 Ultra. I am created by NVIDIA researchers.
#message2:your name  result:I'm Nemotron 3 Ultra, a language model developed by NVIDIA

##   With a higher temperature, the model can produce more variation in its responses.

                    
                    
                    
                    ###Another way for model initialtion

# from langchain_openai/anthropic/google-genai/openrouter import ChatOpenAI/Anthropic/Openrouter

# model = ChatOpenAI(model="gpt-5.6-luna")
# response = model.invoke("Explain recursion in one sentence.")

# print(response.content)                   