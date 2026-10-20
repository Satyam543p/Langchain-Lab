"""
LANGCHAIN CHAT MODEL PROVIDER REFERENCE
"""

from dotenv import load_dotenv

load_dotenv()


# ============================================================
# 1. GOOGLE GEMINI
# Package: pip install -U langchain-google-genai
# Environment variable: GOOGLE_API_KEY
# ============================================================

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # Example model ID; verify current availability.
    temperature=0.2,           # Lower values usually make output more consistent.
    # max_tokens=500,           # Optional response-token limit.
)


# ============================================================
# 2. GROQ
# Package: pip install -U langchain-groq
# Environment variable: GROQ_API_KEY
# ============================================================

from langchain_groq import ChatGroq

model = ChatGroq(
    model="llama-3.3-70b-versatile",  # Example model ID; verify availability.
    temperature=0.2,
    # max_tokens=500,                  # Optional response-token limit.
)


# ============================================================
# 3. OPENROUTER
# Package: pip install -U langchain-openrouter
# Environment variable: OPENROUTER_API_KEY
# ============================================================

model = ChatOpenRouter(
    model="YOUR_OPENROUTER_MODEL_ID",  # Copy a current model ID from OpenRouter.
    temperature=0.2,
    # max_tokens=500,
)


# ============================================================
# 4. OPENAI
# Package: pip install -U langchain-openai
# Environment variable: OPENAI_API_KEY
# ============================================================

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-4.1-mini",  # Example model ID; verify current availability.
    temperature=0.2,
    # max_tokens=500,       # Check integration/model-specific token options.
)


# ============================================================
# 5. ANTHROPIC
# Package: pip install -U langchain-anthropic
# Environment variable: ANTHROPIC_API_KEY
# ============================================================

from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(
    model="claude-3-5-haiku-latest",  # Example ID; verify current availability.
    temperature=0.2,
    # max_tokens=500,                  # Commonly required for Anthropic models.
)


# ============================================================
# 6. OLLAMA — Local models
# Package: pip install -U langchain-ollama
# Requirement: Install Ollama and pull a model first.
# ============================================================

from langchain_ollama import ChatOllama

model = ChatOllama(
    model="llama3.2",  # Example local model; run `ollama pull llama3.2`.
    temperature=0.2,
    # num_predict=500,   # Ollama option that limits generated tokens.
)


# ============================================================
# 7. HUGGING FACE — Hosted endpoint
# Package: pip install -U langchain-huggingface
# Authentication: configure a Hugging Face token for your endpoint.
# ============================================================

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

endpoint = HuggingFaceEndpoint(
    repo_id="YOUR_SUPPORTED_CHAT_MODEL_REPO_ID",
    task="text-generation",
    max_new_tokens=500,
)
model = ChatHuggingFace(llm=endpoint)


# ============================================================
# 8. UNIFIED INITIALIZATION — init_chat_model
# Package: pip install -U langchain
# Install the relevant provider integration as well.
# ============================================================

from langchain.chat_models import init_chat_model

model = init_chat_model(
    "YOUR_PROVIDER_MODEL_ID",
    model_provider="YOUR_PROVIDER",  # e.g. "openai", "anthropic", "google_genai"
    temperature=0.2,
)


# ============================================================
# COMMON USAGE — Works with the selected chat model
# ============================================================

# response = model.invoke("Explain embeddings in two sentences.")
# print(response.content)  # AIMessage.content contains the response text.
#
# For conversation history, pass message objects such as SystemMessage
# and HumanMessage; keep the returned AIMessage when continuing the history.
#
# Useful invocation methods:
#   invoke(input)   -> one result
#   batch(inputs)   -> results for multiple inputs
#   stream(input)   -> stream output chunks as they arrive
#
# Common parameters (support varies by provider/model):
#   temperature -> controls randomness/variability
#   max_tokens  -> limits response length (parameter name may vary)
#   timeout     -> request timeout, where supported
#   max_retries -> retry attempts, where supported
#
# Do not assume every provider supports every parameter or feature.