from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
  # output_dimensionality=768,         # Controls the number of dimensions in the output vector.
  # task_type="SEMANTIC_SIMILARITY",  # Specifies the intended embedding task.
)

text = "LangChain helps developers build LLM applications."

vector = embeddings.embed_query(text)

print("Text:", text)
print("Vector dimensions:", len(vector))
print("First 10 values:", vector[:10])

# Text: LangChain helps developers build LLM applications.
# Vector dimensions: 3072
# First 10 values: [-0.019292492, 0.022621924, 0.022770723, -0.07437863, -0.024601491, 0.014283661, -0.009988247, 0.030375147, 0.02684235, -0.004559631]