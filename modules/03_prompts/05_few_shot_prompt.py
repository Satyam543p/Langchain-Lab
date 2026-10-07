from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

# 1. Examples
examples = [
    {"input": "happy", "output": "positive"},
    {"input": "angry", "output": "negative"},
    {"input": "excited", "output": "positive"}
]

# 2. Template for formatting each example
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input: {input}\nOutput: {output}"
)

# 3. Few-shot prompt
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Input: {input}\nOutput:",
    input_variables=["input"]
)

# 4. Give a new input
prompt = few_shot_prompt.invoke({
    "input": "disappointed"
})

print("#------Generated Prompt------#")
print(prompt)