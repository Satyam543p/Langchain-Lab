from langchain_core.prompts import PromptTemplate,load_prompt

# template
template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_input', 'style_input','length_input'],
validate_template=True
)

template.save('template.json') 

"""through this we can save our prompt in json 
   format and then resuse it easily  by using load_prompt"""


#Using our prompt template saved in json format to create prompt with help of `load_prompt`

template=load_prompt("template.json")
prompt=template.invoke({"paper_input":"...","style_input":"...","length_input":"..."})

print("\n#------prompt------#")
print(prompt)    


# output: text='\nPlease summarize the research paper titled "..." with the following specifications:\nExplanation Style: ...  \nExplanation Length: ...  
#                 \n1. Mathematical Details:  \n   - Include relevant mathematical equations if present in the paper.  \n   - 
#                 Explain the mathematical concepts using simple, intuitive code snippets where applicable.  \n2. Analogies:  \n  - Use relatable analogies to simplify complex ideas.  
#                 \nIf certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
#                  \nEnsure the summary is clear, accurate, and aligned with the provided style and length.\n