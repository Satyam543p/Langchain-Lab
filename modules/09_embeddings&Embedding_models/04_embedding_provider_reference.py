
"""
LANGCHAIN EMBEDDING PROVIDER REFERENCE
"""

from dotenv import load_dotenv

load_dotenv()



# 1. GOOGLE GEMINI


from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    # output_dimensionality=768,       # Controls vector dimensions.
    # task_type="RETRIEVAL_DOCUMENT",   # Embeds documents for retrieval.
)

# Other task types:
# "RETRIEVAL_QUERY"      -> Embed a search query.
# "RETRIEVAL_DOCUMENT"   -> Embed documents for retrieval.
# "SEMANTIC_SIMILARITY"  -> Compare text meaning.
# "CLASSIFICATION"       -> Classification tasks.
# "CLUSTERING"           -> Group similar texts.



# 2. OPENAI


from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    # dimensions=512,  # Optional output dimension for v3 models.
)



# 3. HUGGING FACE — Local embeddings
# Package: langchain-huggingface, sentence-transformers
# Environment variable: Not required for public local models.


from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},  # Run locally on CPU.
    # encode_kwargs={"normalize_embeddings": True},  # Normalize vectors.
)



# 4. OLLAMA — Local embedding models
# Package: langchain-ollama
# Requirement: Ollama installed and model downloaded.


from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    # base_url="http://localhost:11434",  # Custom Ollama server URL.
)



# 5. COHERE


from langchain_cohere import CohereEmbeddings

embeddings = CohereEmbeddings(
    model="embed-english-v3.0",
)



# 6. MISTRAL AI


from langchain_mistralai import MistralAIEmbeddings

embeddings = MistralAIEmbeddings(
    model="mistral-embed",
)



# 7. OPENROUTER — OpenAI-compatible embeddings API


from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="YOUR_OPENROUTER_EMBEDDING_MODEL_ID",
    base_url="https://openrouter.ai/api/v1",
)


# ============================================================
# COMMON USAGE — Works with the selected provider


# text = "LangChain helps build LLM applications."
# vector = embeddings.embed_query(text)
# print("Vector dimensions:", len(vector))
#
# texts = ["Python is useful.", "Java is object-oriented."]
# vectors = embeddings.embed_documents(texts)
# print("Number of vectors:", len(vectors))
# print("Dimensions per vector:", [len(v) for v in vectors])
