from langchain_text_splitters import CharacterTextSplitter

text = """
LangChain is a framework for building applications powered by Large Language Models.
It provides reusable components such as prompts, models, output parsers, and chains.
These components can be connected together to create useful AI workflows.

Document loaders allow us to load data from different sources.
For example, TextLoader reads text files, PyPDFLoader loads PDF documents, and CSVLoader loads CSV data.
The loaded content is represented using LangChain Document objects containing page_content and metadata.

Text splitting is an important step in Retrieval-Augmented Generation (RAG).
Large documents are divided into smaller chunks before they are converted into embeddings.
These embeddings are stored in a vector database and used to retrieve relevant information.

Chunk size controls the target size of each chunk, while chunk overlap allows neighboring chunks to share some text.
Overlap can help preserve context when an important sentence or idea crosses a chunk boundary.
However, excessive overlap can create redundant chunks and increase storage costs.

CharacterTextSplitter divides text using a specified separator.
RecursiveCharacterTextSplitter tries different separators to preserve natural text boundaries where possible.
The best splitting strategy depends on the document structure and the requirements of the application.
"""

splitter=CharacterTextSplitter(    #divide the given text file in chunks fo 200 char 
    chunk_size=200, # max size of chunk
    chunk_overlap=0, # Common sequence of chars
    separator='' # basis on which divison take place
)

chunks=splitter.split_text(text)   #array of divided texts
print('--chunk0--')
print(chunks[0])
# #OUTPUT LangChain is a framework for building applications powered by Large Language Models.
# It provides reusable components such as prompts, models, output parsers, and chains.
# These components can be conne
print()
print('--chunk1--')
print(chunks[1])

# #OUTPUT 
# cted together to create useful AI workflows.

# Document loaders allow us to load data from different sources.
# For example, TextLoader reads text files, PyPDFLoader loads PDF documents, and CSVLoader lo