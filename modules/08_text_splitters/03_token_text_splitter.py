from langchain_text_splitters import TokenTextSplitter,Tokenizer

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

splitter = TokenTextSplitter(          # Splits text based on token count rather than character count, helping control the number of tokens in each chunk.
    encoding_name="cl100k_base",       # Chunk overlap preserves some context between consecutive chunks.
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}:")
    print(chunk)
    print("Character length:", len(chunk))

# Chunk 1:

# LangChain is a framework for building applications powered by Large Language Models.
# It provides reusable components such as prompts, models, output parsers, and chains.
# These components can be connected together to create useful AI workflows.

# Document loaders allow us to load data from different sources.
# For example, TextLoader reads text files, PyPDFLoader loads PDF documents, and CSVLoader loads CSV data.
# The loaded content is represented using LangChain Document objects containing page_content and metadata.

# Text splitting is an important step in
# Character length: 558

# Chunk 2:
#  is represented using LangChain Document objects containing page_content and metadata.

# Text splitting is an important step in Retrieval-Augmented Generation (RAG).
# Large documents are divided into smaller chunks before they are converted into embeddings.
# These embeddings are stored in a vector database and used to retrieve relevant information.

# Chunk size controls the target size of each chunk, while chunk overlap allows neighboring chunks to share some text.
# Overlap can help preserve context when an important sentence or idea crosses a chunk boundary.
# However, excessive overlap can
# Character length: 591

# Chunk 3:
#  can help preserve context when an important sentence or idea crosses a chunk boundary.
# However, excessive overlap can create redundant chunks and increase storage costs.

# CharacterTextSplitter divides text using a specified separator.
# RecursiveCharacterTextSplitter tries different separators to preserve natural text boundaries where possible.
# The best splitting strategy depends on the document structure and the requirements of the application.

# Character length: 449    