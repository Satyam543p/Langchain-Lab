from langchain_core.runnables import RunnableSequence,RunnableLambda

def square(x):
    return x ** 2

square_runnable = RunnableLambda(square)

def double(x):
    return 2 * x

double_runnable = RunnableLambda(double)

chain =RunnableSequence(double_runnable,square_runnable)  #as same as `double_runnable | square_runnable``

result=chain.invoke(5)
print(result)
