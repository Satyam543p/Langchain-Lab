from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

# EXPERIMENT 1: A PROMPT TEMPLATE IS ALSO A RUNNABLE

template = PromptTemplate(
    template="You are a great teacher of {topic}. Explain it.",
    input_variables=["topic"]
)

# .invoke() executes the prompt template and fills its variables.
# No LLM is called here; this step only formats the prompt.
prompt = template.invoke({"topic": "Science"})

print("\n--- EXPERIMENT 1: PromptTemplate ---")
print("Result:", prompt)
print("Python type:", type(prompt))
print("Formatted text:", prompt.to_string())



# EXPERIMENT 2: WRAPPING A PYTHON FUNCTION AS A RUNNABLE


def square(x):
    return x ** 2


# RunnableLambda adapts an ordinary Python function
# to LangChain's Runnable interface.
square_runnable = RunnableLambda(square)

# We can now execute the function through .invoke().
result = square_runnable.invoke(5)

print("\n--- EXPERIMENT 2: RunnableLambda ---")
print("Input:", 5)
print("Output:", result)



# EXPERIMENT 3: COMPOSING RUNNABLES INTO A PIPELINE


def double(x):
    return 2 * x


double_runnable = RunnableLambda(double)

# The pipe operator connects the two Runnable components.
# The output of double_runnable becomes the input of square_runnable.
chain = double_runnable | square_runnable

# One invocation executes the entire pipeline.
result = chain.invoke(5)

print("\n--- EXPERIMENT 3: Runnable Composition ---")
print("Input:", 5)
print("Pipeline: Double -> Square")
print("Expected calculation: (5 * 2) ** 2")
print("Final output:", result)  # 100
