from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnablePassthrough,RunnableParallel

# RunnableParallel sends the same input to every runnable in its mapping.
# Each runnable computes one value, and the final result is a dictionary
# containing those values under their corresponding keys.
r=RunnablePassthrough()

def Uppercase(x):
    return x["text"].upper()

# Both branches receive {'text': 'lovely'}:
# - the "upper" branch transforms the text
# - the "text" branch preserves the original input
chain=RunnableParallel({
    'upper':RunnableLambda(Uppercase),
    'text':RunnablePassthrough()

})

result=chain.invoke({'text':'lovely'})
print(result)

# Expected output:
# {'upper': 'LOVELY', 'text': {'text': 'lovely'}}

