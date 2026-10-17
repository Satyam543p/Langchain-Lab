from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnablePassthrough

# RunnablePassthrough returns exactly the input it receives.
# This is useful in a chain when we want to keep the original value
# available alongside the result of another runnable.
r=RunnablePassthrough()
result=r.invoke({'text': 'Lovely'})

print(result)