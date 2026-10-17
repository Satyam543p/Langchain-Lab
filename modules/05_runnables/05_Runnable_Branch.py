from langchain_core.runnables import RunnableLambda,RunnableBranch

# This runnable converts the input dictionary into a boolean condition.
# Values greater than zero produce True; zero and negative values produce False.
def CheckPositive(x):
    if x['num']>0:
        return True
    return False

CheckPos=RunnableLambda(CheckPositive)

# RunnableBranch checks its conditions from top to bottom and runs the
# runnable attached to the first condition that evaluates to True.
# If no condition matches, the final runnable is used as the default branch.
Branch = RunnableBranch(
    # The input here is the boolean returned by CheckPos.
    (lambda x: x is True, RunnableLambda(lambda x: "Positive")),
    # False represents zero or a negative number in CheckPositive.
    (lambda x: x is False, RunnableLambda(lambda x: "Negative or zero")),
    # This branch is used only if neither condition matches.
    RunnableLambda(lambda x: "Unknown")
)

# The pipeline runs in two stages:
# {'num': 5} -> CheckPos -> True -> Branch -> "Positive"
chain=CheckPos|Branch

result=chain.invoke({'num':5})
print(result)

# Expected output: Positive
