from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loader=PyPDFLoader('./modules/07_Document_loader/sample_handout.pdf')

doc=loader.load()

model=ChatGroq(model_name="qwen/qwen3.8-27b",max_tokens=300)

prompt=PromptTemplate(
    template='Read this page {page} and give us summary about it and key facts',
    input_variables=['page']
)

parser=StrOutputParser()

chain=prompt | model | parser

result=chain.invoke({'page':doc[0].page_content})

print(result)

#OUTPUT
# ### **Summary**
# The page explains the concepts of **Transmission Delay** and **Propagation Delay** in computer networks using a LangChain Loader practice example. It clarifies that these two delays aredistinct: transmission delay is determined by the **size of the packet** and the **transmission rate**, while propagation delay is determined by the **physical distance** and the **speed of signal propagation**. The text emphasizes that a large packet on a short link can have high transmission delay, whereas a small packet on a long-distance link can have high propagation delay. The stated learning objective is to use a PDF loader to inspect both the content and metadata of a PDF document covering this topic.

# ---

# ### **Key Facts**

# 1. **Transmission Delay**:
#    - Definition: Time required to push all packet bits onto the communication link.
#    - Depends on: **Packet size** and **transmission rate**.
#    - Example: A **large packet** can have **high transmission delay** even on a **short link**.

# 2. **Propagation Delay**:
#    - Definition: Time required for a signal to travel from sender to receiver.
#    - Depends on: **Distance** and **propagation speed**.
#    - Example: A **long-distance link** can have **high propagation delay** even for a **small packet**.

