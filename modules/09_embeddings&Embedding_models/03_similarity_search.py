
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

# Initialize the embedding model that converts text into numerical vectors.
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    output_dimensionality=768,  # Controls the number of dimensions per vector.
    # task_type="SEMANTIC_SIMILARITY",  # Specifies the intended embedding task.
)

# Two sentences whose meanings we want to compare.
texts = [
    "I love programming.",
    "Coding is enjoyable."
]

# Generate one embedding vector for each sentence.
vectors = embeddings.embed_documents(texts)

# cosine_similarity() expects 2D inputs: (samples, features).
# [0:1] and [1:2] keep each vector inside a list, preserving its 2D shape.
score = cosine_similarity(vectors[0:1], vectors[1:2])

# Extract the single similarity score from the resulting 2D matrix.
print("Cosine similarity:", score[0][0])


#OUTPUT:  Cosine similarity: 0.9327186557177581
# A score closer to 1 indicates stronger directional similarity.
# It is NOT a percentage or probability that the meanings are identical.

