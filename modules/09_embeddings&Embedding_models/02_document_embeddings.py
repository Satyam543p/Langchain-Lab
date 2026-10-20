from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    output_dimensionality=768,         # Controls the number of dimensions in the output vector.
  # task_type="SEMANTIC_SIMILARITY",  # Specifies the intended embedding task.
)

texts = ["LangChain helps developers build LLM applications.","Your response has been recorded.","The imports used by the experiments are provided by the langchain-text-splitters package."]

vector = embeddings.embed_documents(texts)  # Returns one embedding vector per input text.
print("Number of texts:", len(texts))
print("Number of vectors:", len(vector))
print("Dimensions per vector:", [len(v) for v in vector])
print("First 5 values:", vector[0][:5])

#OUTPUT
# Number of texts: 3
# Number of vectors: 3
# Dimensions per vector: [768, 768, 768]
#First 5 values: [-0.014793866, 0.0155893285, -0.00027488, -0.075633176, -0.00676743]