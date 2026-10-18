from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


loader=WebBaseLoader('https://books.toscrape.com/')

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

### **Summary**
# The page is from **"Books to Scrape,"** a demo website explicitly designed for web scraping practice. It displays a list of **books** available in the store. The view shows the **first 20 results** out of a total of **1,000 products**, spanning **50 pages**.

# Each book entry includes:
# *   **Title** (often truncated with "..." if long)
# *   **Price** in British Pounds (£)
# *   **Stock status** (all listed as "In stock")
# *   An **"Add to basket"** button

# A prominent **warning** states that the website is a **demo for scraping purposes**, and all **prices and ratings are randomly assigned** with no real-world meaning.

# ### **Key Facts**

# | Fact | Detail |
# |------|--------|
# | **Website Purpose** | Demo site for web scraping practice ("We love being scraped!") |
# | **Total Products** | 1,000 books |
# | **Current View** | Showing 1–20 of 1,000 results |
# | **Pagination** | Page 1 of 50 |
# | **Currency** | British Pounds (£) |
# | **Stock Status** | All 20 listed books are "In stock" |