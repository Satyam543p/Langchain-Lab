from langchain_text_splitters import MarkdownHeaderTextSplitter

text="""# LangChain

Introduction to LangChain.

## Document Loaders

Load documents from PDFs, text files, and web pages.

## Text Splitters

Divide long documents into smaller chunks.

### Token Splitting

Split text based on token counts."""

# Splits Markdown documents into sections based on specified heading levels (#, ##, ###).
# Preserves heading information in each Document's metadata to maintain the document's structure.
splitter=MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
)

chunks = splitter.split_text(text)

print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}:")
    print("Content:", chunk.page_content)
    print("Metadata:", chunk.metadata)


# Total chunks: 4

# Chunk 1:
# Content: Introduction to LangChain.
# Metadata: {'Header 1': 'LangChain'}

# Chunk 2:
# Content: Load documents from PDFs, text files, and web pages.
# Metadata: {'Header 1': 'LangChain', 'Header 2': 'Document Loaders'}

# Chunk 3:
# Content: Divide long documents into smaller chunks.
# Metadata: {'Header 1': 'LangChain', 'Header 2': 'Text Splitters'}

# Chunk 4:
# Content: Split text based on token counts.
# Metadata: {'Header 1': 'LangChain', 'Header 2': 'Text Splitters', 'Header 3': 'Token Splitting'}    