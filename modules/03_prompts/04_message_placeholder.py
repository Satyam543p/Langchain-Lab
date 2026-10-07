from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

template=ChatPromptTemplate(
    [
        ('system','You are a helpful customer support agent'),
        MessagesPlaceholder(variable_name='chat_history'),  # here we insert our chat history
        ('human','{query}')
    ]
)
chat_history=[]

with  open("./modules/03_prompts/chat_history.txt") as f:
    chat_history.extend(f.readlines())

print("#-----Chat history-----#\n")
print(chat_history)

print("#-----prompt------#")
prompt=template.invoke({
    "chat_history": chat_history,
    "query": "how are you"
})
print(prompt)    

           #output: messages=[SystemMessage(content='You are a helpful customer support agent', additional_kwargs={}, response_metadata={}),
                            # HumanMessage(content='HumanMessage(content="I want to request a refund for my order #12345.")\n', additional_kwargs={}, response_metadata={}), 
                            # HumanMessage(content='AIMessage(content="Your refund request for order #12345 has been initiated. It will be processed in 3-5 business days.")', additional_kwargs={}, response_metadata={}), 
                            # HumanMessage(content='how areyou', additional_kwargs={}, response_metadata={})]
