from langchain.chat_models import init_chat_model  
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage  #importing types of messages
from dotenv import load_dotenv

load_dotenv()       
model=init_chat_model("nvidia/nemotron-3.5-lightning:free",model_provider="openrouter") #initiating our model



        ##Whole Message concept in shot##


message=[
    SystemMessage(content="You are a concise teacher"),  # to give role or to set behaviour,
    HumanMessage(content="What is a pointer in C?")   #  message by human
]



        ##making two two conversation model to demonstrate what is human message,system mesage and Ai message

print("#-----------------------------#")
print("message:",message) ##show how message is exactly 
print()

print("#-------------AIMessage----------------#")
result=model.invoke(message)

message.append(result)
print()
print("Type of result:",type(result)) #result is AIMessage


print(result.content)
human=input('enter: ')
if human!="\0":
    print()
    print("#--------------SECOND MESSAGE---------------#")
    message.append(HumanMessage(content=human))
    result=model.invoke(message)
    print(result.content)
    print()
    print("Message:",message) ##message after a conversation 

else:print("No request")




