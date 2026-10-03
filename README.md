# 🧪 LangChain Lab

> **A learn-by-building codebase for LangChain** — concept notes, experiments, reusable recipes, and real projects, organized so I can understand, reuse, and keep extending it.

**Learn → Build → Experiment → Understand → Document → Reuse**

| 🧠 Learn | 🛠️ Build | ♻️ Reuse | 🗺️ Decide |
|---|---|---|---|
| Concepts & modules | Complete projects | Reusable recipes | Decision guides |
| Same Task: Baseline → LangChain | Real application patterns | Copy/adapt patterns | Trade-offs & alternatives |

> 💡 **Core philosophy:** This is not a copy-paste tutorial. Every major concept should answer: **what problem exists → solve the same concrete task without LangChain → solve the same task with LangChain → see what LangChain abstracts → compare gains/trade-offs → decide when simpler code is enough.**

---

## 🧭 Quick Navigation

| 🧠 Learn | 🛠️ Build | ♻️ Reuse | 🗺️ Decide |
|---|---|---|---|
| [Concept Guide](#concept-guide) | [Projects](#repository-structure) | [Recipes](#repository-structure) | [Decision Guides](#decision-guides) |
| [Learning Method](#learning-method--progress) | [Modules](#repository-structure) | [How Code Moves](#how-code-moves-through-the-repo) | [Glossary](#glossary) |

---

---

## Table of Contents

1. [TL;DR](#tldr)
2. [How to Use This Repo](#how-to-use-this-repo)
3. [LangChain in 5 Minutes](#langchain-in-5-minutes)
4. [Concept Guide (the 9 modules)](#concept-guide)
5. [Decision Guides](#decision-guides)
6. [Repository Structure](#repository-structure)
7. [How Code Moves Through the Repo](#how-code-moves-through-the-repo)
8. [Documentation Templates](#documentation-templates)
9. [Learning Method & Progress](#learning-method--progress)
10. [Scope & LangGraph](#scope--langgraph)
11. [Glossary](#glossary)
12. [References](#references)

---

## 🧭 TL;DR

> [!NOTE]
> **The repository is a learning system + reusable code library.** Learn concepts in `modules/`, polish repeatable patterns into `recipes/`, and combine them into complete `projects/`.

| Question | Answer |
|---|---|
| What is this? | A structured, hands-on LangChain knowledge base + reusable code library. |
| Who is it for? | Me (as a reference), and anyone who wants to learn LangChain by *understanding*, not copy-pasting. |
| What makes it different? | Every concept answers: **problem → same task without LangChain → same task with LangChain → what changed → trade-offs → when *not* to use it.** |
| Where do I start? | [LangChain in 5 Minutes](#langchain-in-5-minutes), then `modules/01_models/`. |
| Where is reusable code? | `recipes/` (polished, drop-in patterns) and `modules/` (concept code you can also copy from). |
| Where are full apps? | `projects/`. |

---

## 🎯 What You Should Actually Learn

> [!IMPORTANT]
> **Do not optimize for memorizing LangChain APIs. Optimize for understanding the engineering decisions behind them.**

This repository is **not** a memorization exercise.

LangChain's APIs will change. Providers will add features. Some abstractions will move between packages. The durable skill is being able to understand the problem, choose an appropriate level of abstraction, and read the current documentation when implementation details change.

For each concept, aim to understand:

1. **What problem are we solving?**
2. **How would I solve the same concrete task without LangChain?**
3. **What becomes repetitive, fragile, or difficult?**
4. **What abstraction does LangChain provide?**
5. **What exactly do I gain from that abstraction?**
6. **What trade-offs or limitations does it introduce?**
7. **When is it useful?**
8. **When is simpler Python or a provider SDK enough?**
9. **How would I verify the current API in the official documentation?**

> **The goal is to see the same problem solved two ways, understand the abstraction, and then decide whether the abstraction is worth using.**

---

## 📖 How to Use This Repo

| If you want to… | Go to |
|---|---|
| Understand a concept | [Concept Guide](#concept-guide) → then `modules/<NN_concept>/README.md` |
| Copy a working pattern | `recipes/<pattern>/` |
| See concepts combined in a real app | `projects/<app>/` |
| Decide *whether* to use LangChain / agents / RAG | [Decision Guides](#decision-guides) |
| Look up a term | [Glossary](#glossary) |

**Recommended reading order:** this README → `modules/01` → … → `modules/09` → `recipes/` → `projects/`.
The order is a suggestion; jump ahead when a project demands it.

---

## ⚡ LangChain in 5 Minutes

> [!TIP]
> Read this section once to build the mental model. The detailed implementation belongs inside the modules.

### What problem does it solve?

An LLM is a function: **text in → text out**. Real applications need much more around it: working with different providers, structuring prompts and outputs, injecting external data, calling tools, maintaining conversation context, and sometimes coordinating multiple steps.

> **LangChain provides standard interfaces, composition primitives, integrations, and higher-level capabilities for building LLM applications, including agents.**

- **Standard interfaces** — common abstractions for supported chat models, embeddings, vector stores, tools, and other components.
- **Composition** — connect components together (`prompt | model | parser`) with consistent Runnable operations such as `invoke`, `stream`, and `batch`.
- **Integrations** — connect application code to models, document sources, vector stores, tools, and other ecosystem components.
- **Higher-level capabilities** — build patterns such as structured output, retrieval pipelines, tool calling, and agents without implementing every integration yourself.

LangChain does **not** remove every provider-specific difference, and it is not required for every LLM application. One goal of this repository is to understand when its abstractions are useful and when simpler code is enough.

### The mental model

```text
                         ┌────────────────────────────────────────────┐
                         │                Your App                    │
                         └────────────────────────────────────────────┘
                                            │
        ┌──────────┬───────────┬────────────┼────────────┬───────────┬──────────┐
        ▼          ▼           ▼            ▼            ▼           ▼          ▼
     Prompts    Messages    Models     Structured     Retrieval    Tools     Agents
   (templates) (roles &    (chat      output         (RAG)       (functions (loop over
                content)    LLMs)     (schemas)                   the model  model+tools)
                                                                    can call)
        └──────────┴───────────┴── all connected by Runnables (LCEL: `a | b | c`) ──┘
```

### Minimal end-to-end flow

```text
User input → Prompt template → Chat model → Output parser → Result
                  ▲                 │
                  │          (optional) Tool calls ⇄ Tools
                  └── (optional) Retrieved context / chat history
```

### Package map (what to `pip install` and why)

| Package | Contains |
|---|---|
| `langchain` | v1 high-level API: `create_agent`, `init_chat_model`, `init_embeddings`, re-exports of messages/tools |
| `langchain-core` | Base abstractions: Runnables, messages, prompts, output parsers, vector store interface |
| Provider packages (`langchain-openai`, `langchain-anthropic`, …) | Concrete integrations per provider |
| `langchain-community` | Community-maintained integrations (many document loaders, stores) |
| `langchain-text-splitters` | Text splitters used in RAG |
| `langchain-classic` | Legacy pre-v1 APIs (old chains, legacy memory classes) |

### ⚠️ Version note (important when reading tutorials)

LangChain **v1** reduced the main `langchain` namespace to focus on agents and essential building blocks. Many older tutorials use APIs that moved or were replaced:

| Older tutorials | Current (v1) approach |
|---|---|
| `langgraph.prebuilt.create_react_agent` | `langchain.agents.create_agent` |
| `LLMChain`, legacy chains, `ConversationBufferMemory` | LCEL pipelines + checkpointer-based persistence (legacy lives in `langchain-classic`) |
| Provider-specific model classes everywhere | `init_chat_model("<provider>:<model>")` for provider-agnostic setup |

**Rule for this repo:** all code targets the version recorded by that module or recipe. The root README stays mostly conceptual; implementation-specific version details belong in the module/recipe.

Pin versions in each module/recipe (`requirements.txt` / `pyproject.toml`). When an API changes, update the affected module or recipe and document the change when it matters. When current behavior is uncertain, trust the official LangChain documentation for the pinned/current version rather than an older tutorial.

> **Concepts should remain durable even when APIs change.**

---

## 🧩 Concept Guide

> [!IMPORTANT]
> **Official teaching pattern:** every module chooses **one concrete task** and solves that **exact same task twice** — first without LangChain, then with LangChain.

This is the core comparison method of the repository. The point is not to make the baseline artificially bad or the LangChain version artificially impressive. The baseline should be the **simplest meaningful implementation** for the task. Then we can see exactly what LangChain changes.

### 🗺️ The 9-Module Learning Path

```text
FOUNDATION
01 Models
   ↓
02 Messages
   ↓
03 Prompts
   ↓
04 Runnables / LCEL
   ↓
05 Structured Output

APPLICATION PATTERNS
   ↓
06 RAG
   ↓
07 Memory
   ↓
08 Tools
   ↓
09 Agents
```

| # | Module | Main question | Same-task comparison |
|---:|---|---|---|
| 01 | 🤖 **Models** | How do I interact with different model providers? | Send the same question to a model and compare the direct SDK approach with LangChain's common model interface. |
| 02 | 💬 **Messages** | How should conversational input/output be represented? | Send the same system + user conversation using provider-style message data vs. LangChain message objects. |
| 03 | ✍️ **Prompts** | How do I create reusable, parameterized prompts? | Generate the same tutor prompt from the same `role`, `topic`, and `question` inputs. |
| 04 | 🔗 **Runnables / LCEL** | How do I compose LLM steps cleanly? | Run the same `prompt → model → parse` workflow manually vs. as a Runnable pipeline. |
| 05 | 📦 **Structured Output** | How do I turn model output into predictable data? | Extract the same support ticket into the same fields, once with manual JSON parsing and once with a schema. |
| 06 | 🔎 **RAG** | How do I give the model relevant external knowledge? | Answer the same question from the same documents using a hand-built retrieval flow vs. LangChain components. |
| 07 | 🧠 **Memory** | How does an application retain conversation state? | Run the same three-turn conversation while manually managing history vs. using framework-supported state/history. |
| 08 | 🛠️ **Tools** | How can a model request real-world functions/actions? | Handle the same word-count request with a manual tool-call dispatcher vs. LangChain tool definitions and binding. |
| 09 | 🤖 **Agents** | How can the model decide which tools/steps to use? | Complete the same multi-tool task with a hand-written model/tool loop vs. a LangChain agent. |

### 🔍 How the Same-Task Comparison Works

For every module, use this sequence:

```text
             ┌──────────────────────────┐
             │  1. Define one task      │
             │  exact input + goal      │
             └────────────┬─────────────┘
                          │
             ┌────────────▼─────────────┐
             │ 2. Without LangChain     │
             │ simplest meaningful     │
             │ baseline implementation  │
             └────────────┬─────────────┘
                          │
             ┌────────────▼─────────────┐
             │ 3. With LangChain        │
             │ same input + same goal   │
             └────────────┬─────────────┘
                          │
             ┌────────────▼─────────────┐
             │ 4. What actually changed?│
             │ abstraction + glue code  │
             └────────────┬─────────────┘
                          │
             ┌────────────▼─────────────┐
             │ 5. Trade-offs            │
             │ complexity / control /   │
             │ portability / features   │
             └────────────┬─────────────┘
                          │
             ┌────────────▼─────────────┐
             │ 6. When is each approach │
             │ the simpler fit?         │
             └──────────────────────────┘
```

> 💡 **Fair comparison rule:** keep the **input, expected behavior, provider/model, and important settings** as comparable as practical. Do not change the task just to make one implementation look better.

> 💡 **The baseline is not always “plain Python.”** It may be a provider SDK, manual JSON handling, a custom function pipeline, a hand-written tool dispatcher, or a hand-built agent loop. The goal is to compare against the simplest real alternative.

> 💡 **No forced `raw_python.py`.** Small comparisons belong directly in the module README. Create executable baseline code only when it is useful for experiments or debugging.

---

### 01 · Models

| | |
|---|---|
| **Problem** | Provider SDKs expose different interfaces, configuration styles, and response objects. Application code can therefore become coupled to a provider. |
| **Same task** | Send **“Explain recursion in one sentence.”** to OpenAI and print the answer. |
| **Comparison** | **OpenAI SDK** vs **LangChain's model interface** — same provider, same model, same input. |

> 🎯 **Why this is a useful comparison:** we are not comparing two unrelated examples. Both implementations perform the **exact same task** with OpenAI. The difference is the abstraction used by the application.

**🦜 With LangChain — first:**
```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-5.6-luna")
response = model.invoke("Explain recursion in one sentence.")

print(response.content)
```

**🐍 Without LangChain — OpenAI SDK:**
```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.6-luna",
    input="Explain recursion in one sentence.",
)

print(response.output_text)
```

### 🔍 What Changed?

| Step | OpenAI SDK | LangChain |
|---|---|---|
| Client/model object | `OpenAI()` + Responses API | `ChatOpenAI(...)` |
| Main call | `client.responses.create(...)` | `model.invoke(...)` |
| Response extraction | `response.output_text` | `response.content` |
| Application abstraction | OpenAI-specific | LangChain chat-model interface |
| Provider portability | OpenAI details are visible here | Supported providers can expose the same higher-level model operations |

**What LangChain actually solved:** it puts a common model interface between application code and provider integrations. The value becomes much clearer when the application grows beyond one simple model call.

**What it did not solve:** provider capabilities and behavior are not identical. You can still need provider-specific options, provider-specific features, or integration-specific setup.

**Key ideas:** `ChatOpenAI`, `invoke`, `stream`, `batch`, model configuration, provider integrations.

**Pitfalls:** do not assume every model supports every feature; response content can have richer structures than plain text; API keys belong in environment variables.

**When the simpler approach is enough:** a tiny app that intentionally targets only OpenAI may find the official SDK more direct and easier to learn.

---

### 02 · Messages

| | |
|---|---|
| **Problem** | A chat request needs roles such as system/user/assistant. Provider APIs represent those messages with their own input structures. |
| **Same task** | Send the same conversation: **system = “You are a concise tutor.”** and **user = “What is a pointer in C?”** |
| **Without LangChain** | Build the OpenAI message input manually as dictionaries and pass it to the SDK. |
| **With LangChain** | Build typed message objects and pass them to the model interface. |

**🦜 With LangChain — first:**
```python
from langchain.messages import SystemMessage, HumanMessage

messages = [
    SystemMessage(content="You are a concise tutor."),
    HumanMessage(content="What is a pointer in C?"),
]

response = model.invoke(messages)
print(response.content)
```

**🐍 Without LangChain — OpenAI SDK:**
```python
from openai import OpenAI

client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "You are a concise tutor.",
    },
    {
        "role": "user",
        "content": "What is a pointer in C?",
    },
]

response = client.responses.create(
    model="gpt-5.6-luna",
    input=messages,
)

print(response.output_text)
```

### 🔍 What Changed?

| Step | Without LangChain | With LangChain |
|---|---|---|
| Role representation | Provider input dictionaries | Typed message objects |
| Message construction | Manual | Explicit message classes |
| Model call | Provider-specific SDK | Common model interface |
| Reuse across integrations | Your own conventions | Shared LangChain message model |

**What LangChain actually solved:** it gives your application a common representation for conversational messages instead of making every part of the codebase speak a provider's raw message format.

**What it did not solve:** message order, context selection, token limits, and conversation-state design are still application responsibilities.

**Key ideas:** `SystemMessage`, `HumanMessage`, `AIMessage`, `ToolMessage`, message order, message content.

**Pitfalls:** do not confuse messages with memory; messages are the data, while memory/state is the strategy for storing and supplying that data over time.

**When the simpler approach is enough:** a single-provider application can reasonably use the provider's native message dictionaries directly.

---

### 03 · Prompts

| | |
|---|---|
| **Problem** | Repeated string interpolation becomes messy when the same prompt needs variables, roles, formatting, and later composition. |
| **Same task** | Create the same tutor prompt from `role`, `topic`, and `question`. |
| **Without LangChain** | Build the string manually with Python formatting. |
| **With LangChain** | Represent the prompt as a reusable template with named inputs. |

**🦜 With LangChain — first:**
```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a {role}. The topic is {topic}."),
    ("human", "Answer this question briefly: {question}"),
])

messages = prompt.invoke({
    "role": "CSE tutor",
    "topic": "recursion",
    "question": "What is a base case?",
})

print(messages)
```

**🐍 Without LangChain:**
```python
role = "CSE tutor"
topic = "recursion"
question = "What is a base case?"

prompt = (
    f"You are a {role}. "
    f"The topic is {topic}. "
    f"Answer this question briefly: {question}"
)

print(prompt)
```

### 🔍 What Changed?

| Step | Without LangChain | With LangChain |
|---|---|---|
| Variables | Manual interpolation | Named template variables |
| Message structure | Built into strings | Explicit prompt/message template |
| Reuse | Your own convention | First-class reusable component |
| Composition | Manual | Ready to participate in Runnable pipelines |

**What LangChain actually solved:** prompt construction becomes an explicit component with declared inputs, rather than just a string built somewhere in application code.

**What it did not solve:** prompt quality. A bad template is still a bad prompt, and changing wording can change application behavior.

**Key ideas:** prompt templates, message templates, input variables, partial/composed prompts.

**Pitfalls:** missing variables cause errors; literal braces can require escaping; changing a template can be a behavioral change even when Python code stays identical.

**When the simpler approach is enough:** one fixed prompt used once is often clearer as a normal string.

---

### 04 · Runnables / LCEL

| | |
|---|---|
| **Problem** | A multi-step LLM workflow creates glue code when each step is called manually and each step has a different calling convention. |
| **Same task** | Do the same pipeline: **build prompt → call model → convert reply to string**. |
| **Without LangChain** | Call functions one-by-one and pass each result yourself. |
| **With LangChain** | Compose compatible components into one Runnable pipeline. |

**🦜 With LangChain — first:**
```python
from langchain_core.output_parsers import StrOutputParser

chain = prompt | model | StrOutputParser()

answer = chain.invoke({
    "role": "CSE tutor",
    "topic": "recursion",
    "question": "Explain recursion in one sentence.",
})

print(answer)
```

**🐍 Without LangChain:**
```python
def make_prompt(role, topic, question):
    return (
        f"You are a {role}. The topic is {topic}. "
        f"Answer briefly: {question}"
    )


def call_model(prompt_text):
    # This is where the provider SDK call lives.
    return provider_call(prompt_text)


def parse_response(response):
    # You must decide what the provider response object means.
    return response.output_text.strip()


prompt_text = make_prompt(
    role="CSE tutor",
    topic="recursion",
    question="Explain recursion in one sentence.",
)

raw_response = call_model(prompt_text)
answer = parse_response(raw_response)
print(answer)
```

> The baseline looks longer because **you now own the glue**: function boundaries, result passing, response extraction, and the conventions between steps.

### 🔍 What Changed?

| Step | Without LangChain | With LangChain |
|---|---|---|
| Step execution | Explicit Python calls | Runnable composition |
| Data passing | Manual | Standardized between compatible steps |
| Reuse | Your own pipeline conventions | A composable chain |
| Streaming/batching/async | Your own orchestration | Common Runnable operations |

**What LangChain actually solved:** a common execution model for components, so you can compose a workflow instead of repeatedly inventing glue code.

**What it did not solve:** data-shape mistakes, business logic, external failures, latency, or application-specific orchestration decisions.

**Key ideas:** `Runnable`, `invoke`, `stream`, `batch`, `ainvoke`, `RunnableLambda`, `RunnableParallel`, composition.

**Pitfalls:** the output shape of one component must match the next component's expected input; inspect intermediate values while learning.

**When the simpler approach is enough:** one or two direct function calls are often easier to read as ordinary Python.

---

### 05 · Structured Output

| | |
|---|---|
| **Problem** | Free-form model text is awkward to consume safely because the application needs predictable fields and types. |
| **Same task** | Extract the support ticket into `title` and `priority` from: **“Login page crashes for all users since the update!”** |
| **Without LangChain** | Ask for JSON, parse it, then perform your own schema/type checks. |
| **With LangChain** | Define the schema and let the model integration return the structured object. |

**🦜 With LangChain — first:**
```python
from pydantic import BaseModel, Field


class Ticket(BaseModel):
    title: str = Field(description="Short summary of the issue")
    priority: int = Field(description="1 (low) to 5 (urgent)")


structured_model = model.with_structured_output(Ticket)

ticket = structured_model.invoke(
    "Login page crashes for all users since the update!"
)

print(ticket)
```

**🐍 Without LangChain:**
```python
import json

raw = provider_call(
    "Return ONLY JSON with exactly these fields: "
    "title (string) and priority (integer 1-5).\n\n"
    "Ticket: Login page crashes for all users since the update!"
)

# You now have to do all of this yourself.
data = json.loads(raw)

if not isinstance(data.get("title"), str):
    raise ValueError("title must be a string")

if not isinstance(data.get("priority"), int):
    raise ValueError("priority must be an integer")

if not 1 <= data["priority"] <= 5:
    raise ValueError("priority must be between 1 and 5")

print(data)
```

> The point of the baseline is visible here: **getting JSON text is not the same as getting application-ready structured data**. You must parse and validate it yourself.

### 🔍 What Changed?

| Step | Without LangChain | With LangChain |
|---|---|---|
| Desired structure | Describe it in the prompt | Define a schema |
| Parsing | `json.loads()` | Structured-output integration |
| Type validation | Manual | Schema/Pydantic validation |
| Application handoff | Dict + custom checks | Typed object |

**What LangChain actually solved:** it connects the model call to a declared output schema and structured parsing/validation behavior.

**What it did not solve:** semantic correctness. A response can be perfectly shaped and still contain the wrong title or priority.

**Key ideas:** Pydantic, schemas, field descriptions, parsing, validation.

**Pitfalls:** support varies by model/provider; malformed or semantically wrong content can still require application checks.

**When the simpler approach is enough:** a small script with strong provider-native structured-output support may be clearer without another abstraction layer.

---

### 06 · RAG (Retrieval-Augmented Generation)

| | |
|---|---|
| **Problem** | A model may need private or changing documents without sending the entire document collection every time. |
| **Same task** | Using the **same document set**, answer: **“What is the refund policy?”** |
| **Without LangChain** | Implement loading, chunking, embedding, search, context construction, and the final model call yourself. |
| **With LangChain** | Use reusable loaders/splitters/embeddings/vector stores/retrievers and compose the retrieval flow. |

**🦜 With LangChain — first:**
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore

chunks = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
).split_documents(docs)

store = InMemoryVectorStore(embeddings)
store.add_documents(chunks)
retriever = store.as_retriever(search_kwargs={"k": 4})

relevant_docs = retriever.invoke("What is the refund policy?")
context = "\n\n".join(doc.page_content for doc in relevant_docs)

answer = model.invoke(
    f"Answer using only this context:\n\n{context}\n\n"
    "Question: What is the refund policy?"
)

print(answer.content)
```

**🐍 Without LangChain:**
```python
import math
from collections import Counter


def tokenize(text):
    return text.lower().split()


def split_into_chunks(text, size=80):
    words = tokenize(text)
    return [words[i:i + size] for i in range(0, len(words), size)]


def score(query_words, chunk_words):
    query = Counter(query_words)
    chunk = Counter(chunk_words)
    common = sum((query & chunk).values())
    return common / math.sqrt((sum(query.values()) or 1) * (sum(chunk.values()) or 1))


# Same document set, but all retrieval plumbing is yours.
chunks = []
for doc in documents:
    chunks.extend(split_into_chunks(doc))

query_words = tokenize("What is the refund policy?")
ranked = sorted(
    chunks,
    key=lambda chunk: score(query_words, chunk),
    reverse=True,
)

context = "\n".join(" ".join(chunk) for chunk in ranked[:4])
answer = provider_call(
    "Answer using only this context:\n"
    f"{context}\n\nQuestion: What is the refund policy?"
)

print(answer.output_text)
```

> This baseline deliberately exposes the work LangChain is helping you organize: **document preparation → representation → retrieval → context assembly → generation**.

### 🔍 What Changed?

| Step | Without LangChain | With LangChain |
|---|---|---|
| Loading | Your own code/provider SDK | Loader integrations |
| Splitting | Custom functions | Reusable text splitters |
| Embeddings | Direct embedding API | Common embedding interface |
| Search | Your own index/query logic | Vector-store + retriever abstractions |
| Glue | Hand-written | Composable retrieval workflow |

**What LangChain actually solved:** integration and composition across common RAG building blocks.

**What it did not solve:** retrieval quality. Chunking, embedding choice, ranking, metadata, evaluation, permissions, and prompt design still determine whether the retrieved context is useful.

**Key ideas:** document → chunk → embedding → vector store → retriever → context → generation.

**Pitfalls:** inconsistent embeddings hurt retrieval; poor chunking can lose context; in-memory stores disappear on restart; retrieval can return irrelevant material.

**When the simpler approach is enough:** a small stable dataset that fits comfortably in context may be simpler to provide directly.

---

### 07 · Memory

| | |
|---|---|
| **Problem** | A follow-up question needs relevant earlier conversation state to be available on the next call. |
| **Same task** | Run the same three turns: **T1:** “My name is Satyam.” → **T2:** “What is my name?” → **T3:** “Now answer in one word.” |
| **Without LangChain** | Store messages yourself and resend the required history. |
| **With LangChain** | Use the framework-supported state/persistence pattern for the LangChain version and integration being studied. |

**🦜 With LangChain — first:**
```text
session / thread id
        ↓
stored conversation state
        ↓
LangChain-facing model/agent call
        ↓
updated state
        ↓
next turn uses the stored conversation
```

```python
# Conceptual learning example.
# The exact persistence API depends on the LangChain integration/version.

thread_id = "student-001"

result_1 = application.invoke(
    {"messages": [{"role": "user", "content": "My name is Satyam."}]},
    config={"configurable": {"thread_id": thread_id}},
)

result_2 = application.invoke(
    {"messages": [{"role": "user", "content": "What is my name?"}]},
    config={"configurable": {"thread_id": thread_id}},
)

result_3 = application.invoke(
    {"messages": [{"role": "user", "content": "Now answer in one word."}]},
    config={"configurable": {"thread_id": thread_id}},
)
```

**🐍 Without LangChain:**
```python
from openai import OpenAI

client = OpenAI()
history = []


def ask(user_text):
    history.append({"role": "user", "content": user_text})

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=history,
    )

    # You must keep assistant output in your own state.
    history.append({"role": "assistant", "content": response.output_text})
    return response.output_text


print(ask("My name is Satyam."))
print(ask("What is my name?"))
print(ask("Now answer in one word."))
```

> The key difference is visible in the baseline: **you own the history data structure, persistence policy, trimming strategy, and session identity**.

### 🔍 What Changed?

| Step | Without LangChain | With LangChain |
|---|---|---|
| History storage | Your own list/database | Framework-supported state/checkpoint pattern |
| Session identity | Your own convention | Thread/session identifier |
| Persistence | Your responsibility | Supported through the chosen persistence integration |
| Trimming/summarization | Your code | Still an application design concern |

**What LangChain actually solved:** it gives a framework-level way to carry conversation state alongside the application workflow.

**What it did not solve:** deciding what should be remembered, how long it should live, privacy/isolation, and the cost of unbounded history.

**Key ideas:** short-term state, session/thread identity, persistence, trimming, summarization, long-term memory as a separate design.

**Pitfalls:** unbounded history increases tokens and cost; persistence is not magic—you still need an appropriate storage/checkpoint mechanism.

**When the simpler approach is enough:** a small single-session script can often use a Python list.

---

### 08 · Tools

| | |
|---|---|
| **Problem** | A model can request an action, but your application must describe the function, inspect the request, execute it, and return the result. |
| **Same task** | Answer: **“How many words are in ‘to be or not to be’?”** using `get_word_count(text)`. |
| **Without LangChain** | Define the tool schema and dispatch/response handling yourself. |
| **With LangChain** | Turn a Python function into a tool and bind it to the model. |

**🦜 With LangChain — first:**
```python
from langchain.tools import tool


@tool
def get_word_count(text: str) -> int:
    """Count the number of words in the given text."""
    return len(text.split())


model_with_tools = model.bind_tools([get_word_count])

ai_message = model_with_tools.invoke(
    "How many words are in 'to be or not to be'?"
)

print(ai_message.tool_calls)
```

> **Important:** binding a tool does **not** execute it. The model can request a tool call; an application/agent still has to run the function and provide the result.

**🐍 Without LangChain:**
```python
def get_word_count(text: str) -> int:
    return len(text.split())


TOOLS = {
    "get_word_count": get_word_count,
}

# A provider response may contain a tool name + JSON arguments.
request = parse_provider_tool_call(model_response)

if request.name not in TOOLS:
    raise ValueError(f"Unknown tool: {request.name}")

result = TOOLS[request.name](**request.arguments)

tool_message = make_provider_tool_result(
    call_id=request.call_id,
    result=result,
)

# You then send the tool result back to the provider if another model
# turn is required.
```

> The baseline exposes the real problem: **tool calling is more than writing a function**. You also need a schema, validation, dispatch, a result message, and often another model turn.

### 🔍 What Changed?

| Step | Without LangChain | With LangChain |
|---|---|---|
| Tool definition | Manual schema + convention | Typed Python function + decorator |
| Tool-call representation | Provider-specific | Common tool-call object |
| Dispatch | Custom parser/registry | Framework-supported integration |
| Execution | Your code | Still your code/agent; LangChain helps wire the interaction |

**What LangChain actually solved:** more uniform tool definition and model/tool integration.

**What it did not solve:** authorization, business rules, side-effect safety, or whether an action should be permitted.

**Key ideas:** tool schema, tool call, tool result, `@tool`, `bind_tools`, validation.

**Pitfalls:** validate arguments, protect side effects, keep descriptions precise, and limit overlapping tools.

**When the simpler approach is enough:** one small function plus a provider-native tool-calling API may not justify another abstraction.

---

### 09 · Agents

| | |
|---|---|
| **Problem** | Some tasks need the application to let the model decide which tool to call, whether another step is needed, and when to stop. |
| **Same task** | Given **“Count the words in ‘hello big world’ and also give me the uppercase version.”**, use two tools and return both results. |
| **Without LangChain** | Write the model → tool → result loop and stop conditions yourself. |
| **With LangChain** | Use a higher-level agent abstraction for that recurring loop. |

**🦜 With LangChain — first:**
```python
from langchain.agents import create_agent

agent = create_agent(
    model=model,
    tools=[get_word_count, uppercase_text],
)

result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": (
                "Count the words in 'hello big world' "
                "and also give me the uppercase version."
            ),
        }
    ]
})

print(result)
```

**🐍 Without LangChain:**
```python
def run_agent(messages):
    for step in range(5):  # application-defined safety limit
        response = provider_model_call(messages)

        if not response.tool_calls:
            return response.text

        for call in response.tool_calls:
            tool = TOOL_REGISTRY.get(call.name)
            if tool is None:
                raise ValueError(f"Unknown tool: {call.name}")

            arguments = validate_tool_arguments(call.name, call.arguments)
            tool_result = tool(**arguments)

            messages.append(response.as_message())
            messages.append(
                make_tool_result_message(call.id, tool_result)
            )

    raise RuntimeError("Agent exceeded the maximum number of steps")
```

> This is where the difference becomes large: the baseline forces you to design the **loop, tool routing, result messages, validation, step limits, and termination behavior**.

### 🔍 What Changed?

| Step | Without LangChain | With LangChain |
|---|---|---|
| Loop | Hand-written | Ready-made agent runtime |
| Tool routing | Custom | Framework-supported |
| Repeated calls | Custom loop | Agent orchestration |
| Safety/limits | Your implementation | Still requires your configuration/guardrails |
| Control | Fully explicit | Higher-level abstraction |

**What LangChain actually solved:** it packages a common model → tool → observation/result → next model decision loop so you do not rebuild the orchestration mechanism from scratch.

**What it did not solve:** reliability, permissions, evaluation, latency/cost control, or application-specific guardrails.

**Key ideas:** agent, tool selection, repeated action loop, stop condition, guardrails.

**Pitfalls:** agent behavior can be less predictable than a fixed workflow; tool use can increase latency/cost; always test and cap loops.

**When the simpler approach is enough:** when the exact steps are already known, a fixed workflow can be easier to understand and test than an agent.

---

## 🧠 Decision Guides

> [!IMPORTANT]
> These are **trade-off guides**, not rankings. The right choice depends on the application's requirements.

### Raw Python vs. Provider SDK vs. LangChain

```text
One model, one call, simple logic?            → Provider SDK or plain Python
Need provider switching / uniform interface?  → LangChain
Need prompts + parsing + retrieval + tools?   → LangChain (composition pays off)
Complex stateful loops, branching, recovery?  → LangGraph (separate repo)
```

### Workflow vs. Agent

```text
Do I know the steps in advance?
   YES → Workflow / chain   (predictable, cheaper, testable)
   NO  → Agent              (flexible, costlier, needs guardrails)
```

### RAG vs. Long Context

```text
Data small & stable, fits in context?   → put it in the prompt (simpler)
Data large / changing / private?        → RAG
Need citations of which source was used?→ RAG (retrieved chunks are traceable)
```

### Do I need memory?

```text
Single-turn Q&A?                         → No
Follow-ups depend on earlier turns?      → Yes (short-term, per thread)
Facts must persist across sessions?      → Yes (long-term, external storage)
```

---

## 🔎 When I Need Something Later

> [!TIP]
> Treat this repository as your personal engineering reference. Don't start from zero every time you need a feature.

Use this repository as a working knowledge base, not just a course.

```text
I need a feature
      │
      ▼
Do I understand the concept?
      │
   ┌──┴──┐
   NO   YES
   │      │
   ▼      ▼
modules/  Is there already a recipe?
           │
        ┌──┴──┐
       YES    NO
        │      │
        ▼      ▼
   reuse/adapt  build/experiment
   recipes/     in modules/
                   │
                   ▼
             Stable + reusable?
                   │
                  YES
                   │
                   ▼
             polish into
              recipes/
                   │
                   ▼
              use in a
             projects/
```

The practical rule is:

- **Don't understand it yet?** Start in `modules/`.
- **Already understand it and a recipe exists?** Reuse or adapt the recipe.
- **No recipe exists?** Build and experiment in the relevant module first.
- **The pattern proves stable and reusable?** Polish it into `recipes/`.
- **You're building a complete application?** Put it in `projects/`.

This keeps the repository useful both for learning something for the first time and for finding an implementation months later.

---

## 📁 Repository Structure

The repository is intentionally divided into four layers:

```text
langchain-lab/
│
├── 📄 README.md
├── 📄 requirements.txt             # Shared learning environment
├── 📄 .env.example                 # Safe configuration template
├── 🔒 .env                         # Local secrets; NEVER commit
├── 📄 .gitignore
│
├── ⚙️ core/
│   ├── 📄 README.md                  # What belongs in core and why
│   └── 📄 config.py                  # Shared config/env helpers, only when genuinely needed
│
├── 🧩 modules/
│   ├── 01_models/
│   │   ├── 📄 README.md              # Concept lesson + same-task comparison
│   │   └── 📄 examples.py            # Optional executable examples
│   │
│   ├── 02_messages/
│   │   ├── 📄 README.md
│   │   └── 📄 examples.py
│   │
│   ├── 03_prompts/
│   │   ├── 📄 README.md
│   │   └── 📄 examples.py
│   │
│   ├── 04_runnables/
│   │   ├── 📄 README.md
│   │   └── 📄 examples.py
│   │
│   ├── 05_structured_output/
│   │   ├── 📄 README.md
│   │   └── 📄 examples.py
│   │
│   ├── 06_rag/
│   │   ├── 📄 README.md
│   │   ├── 📄 examples.py
│   │   └── 🧪 experiments/
│   │
│   ├── 07_memory/
│   │   ├── 📄 README.md
│   │   └── 📄 examples.py
│   │
│   ├── 08_tools/
│   │   ├── 📄 README.md
│   │   └── 📄 examples.py
│   │
│   └── 09_agents/
│       ├── 📄 README.md
│       └── 📄 examples.py
│
├── ♻️ recipes/
│   ├── simple_chat/
│   │   ├── 📄 README.md              # What it solves, when to use it, limitations
│   │   ├── 📄 recipe.py              # Clean reusable implementation
│   │   ├── 📄 requirements.txt       # Dependencies/version pinning when needed
│   │   └── 📄 .env.example           # Only when environment variables are required
│   │
│   ├── structured_extraction/
│   │   ├── 📄 README.md
│   │   ├── 📄 recipe.py
│   │   └── 📄 requirements.txt
│   │
│   ├── basic_rag/
│   │   ├── 📄 README.md
│   │   ├── 📄 recipe.py
│   │   └── 📄 requirements.txt
│   │
│   ├── conversational_rag/
│   ├── tool_calling/
│   └── simple_agent/
│
└── 🚀 projects/
    └── <project-name>/
        ├── 📄 README.md              # Product, architecture, decisions & trade-offs
        ├── 📄 requirements.txt       # Or pyproject.toml
        ├── 📄 .env.example           # Required environment variables
        ├── 📁 src/                    # Application code
        ├── 📁 tests/                  # Tests when the project needs them
        └── 📁 assets/                 # Optional project-specific files/data
```

### What the files are for

| Location | File / folder | Why it exists |
|---|---|---|
| Root | `README.md` | The repository's map, philosophy, roadmap, and decision guide. |
| Root | `requirements.txt` | Shared dependency set for the learning environment. Start with one file rather than creating dependency files for every module/recipe. |
| Root | `.env.example` | Safe template showing which environment variables may be needed. Commit this file; never put real secrets in it. |
| Root | `.env` | Your local API keys/configuration. **Never commit it.** |
| Root | `.gitignore` | Keeps `.env`, caches, virtual environments, and other local files out of Git. |
| `core/` | `README.md` | Documents what is allowed in `core/` so it does not become a dumping ground. |
| `core/` | `config.py` | Shared configuration/environment logic **only when multiple parts genuinely need it**. It does not have to exist on day one. |
| Every module | `README.md` | The actual concept lesson: problem, same task, baseline implementation, LangChain implementation, experiments, pitfalls, and trade-offs. |
| Every module | `README.md` | The main learning document, including the **same-task** baseline vs. LangChain comparison. |
| Module | `examples.py` | Optional executable LangChain examples when code is useful; the filename is a convention, not a requirement. |
| Module | `experiments/` | Optional experiments, variations, failure cases, and "what happens if I change/break this?" work. |
| Every recipe | `README.md` | How to use the pattern, when to use/skip it, inputs/outputs, and limitations. |
| Every recipe | `recipe.py` | The polished implementation intended to be copied/adapted. |
| Recipe | `.env.example` | Only when a recipe genuinely needs configuration that should be documented separately; otherwise use the root `.env.example`. |
| Every project | `README.md` | What the application does, architecture, components, decisions, and trade-offs. |
| Project | `src/` | Application-specific source code. |
| Project | `tests/` | Tests for meaningful application behavior. |
| Project | `requirements.txt` | Optional project-specific dependencies when the project needs isolation from the shared learning environment. |
| Project | `.env.example` | Optional project-specific configuration template when the project's environment differs from the root setup. |

> [!IMPORTANT]
> **The exact files are allowed to grow.** The tree above is a recommended starting convention, not a rule that every module must have every file. Start with the shared root `.env` and `requirements.txt`; introduce per-project configuration or dependencies only when there is a real reason.

### A few important rules

**`README.md` is the explanation and comparison.**  
**The baseline implementation lives in the README when it is useful for teaching.**  
**`examples.py` (or another focused file) contains executable LangChain code when needed.**  
**`experiments/` is where understanding is tested.**  
**`recipe.py` is the polished reusable pattern.**  
**`src/` is application-specific project code.**

A module may need additional files. For example, RAG may eventually have separate files for ingestion, retrieval, evaluation, or vector-store experiments. Do not force everything into one `langchain.py` if splitting the code makes the concept clearer.

### 🔐 Configuration & Dependencies

For this learning repository, **start centralized and isolate only when there is a reason**.

```text
                    langchain-lab/
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        .env.example          requirements.txt
              │                     │
              ▼                     ▼
       .env (local only)     shared learning environment
              │
              ▼
       modules / recipes
```

#### Environment variables

Use **one root `.env`** for local development:

```env
OPENAI_API_KEY=
GOOGLE_API_KEY=
ANTHROPIC_API_KEY=
```

Commit **`.env.example`**, but never commit the real `.env`.

```text
.env.example  → GitHub ✅
.env          → local machine only 🔒
```

The root `.env.example` should contain variable names and safe placeholders, not real credentials.

A recipe normally uses the root `.env.example`. Give a recipe its own `.env.example` only when it genuinely requires configuration that is different enough to document separately.

#### Dependencies

Start with **one root `requirements.txt`** for the shared learning environment.

```text
modules/  ──┐
recipes/  ──┼──► root requirements.txt
            │
            └──► shared environment
```

Do not create a `requirements.txt` for every module or recipe just because the folder contains Python code.

A project may get its own `requirements.txt` (or `pyproject.toml`) when it becomes sufficiently independent or needs dependencies that should not be part of the shared learning environment.

> **Rule:** Centralize while the repository is simple. Introduce per-project isolation when the project actually needs it.

### Folder responsibilities

| Folder | Purpose | Code quality bar | Question it answers |
|---|---|---|---|
| ⚙️ `core/` | Genuinely shared infrastructure. **Starts tiny and grows only when justified.** | Stable | "What do multiple parts genuinely need in common?" |
| 🧩 `modules/` | **Learn & understand** one concept. Includes explanations, baseline implementations, and experiments. | Educational, usable | "How does this work?" |
| ♻️ `recipes/` | **Ready-to-adapt** implementation of a common pattern, polished and documented. | Reusable | "I need this. How do I implement it?" |
| 🚀 `projects/` | **Build** complete applications combining concepts. | Application-grade | "How do the pieces work together?" |

> **Modules are reusable too.** A module can absolutely be copied or imported later. The difference is purpose: a module is organized around *understanding*, while a recipe is the cleaned-up, documented pattern intended for repeated use.

> **The README is the main teaching surface.** The same-task comparison belongs here so you do not have to maintain duplicate `raw_python.py` files for nine modules. Create executable comparison code only when the experiment is substantial enough to justify it.

### About `projects/`

Projects are not predefined. A folder is added when a real project is actually built.

Each project should normally contain:

- `README.md` — architecture, decisions, setup, and usage
- `src/` — application code
- `tests/` — tests where useful
- `assets/` — optional project-specific resources
- `requirements.txt` or `pyproject.toml` — **only when the project needs its own dependency set**
- `.env.example` — **only when the project needs project-specific configuration**; otherwise use the root `.env.example`

Typical examples are illustrations, not a fixed roadmap:

| Project type | Concepts it combines |
|---|---|
| Chat with your PDFs / notes | Models + Prompts + RAG |
| Support or FAQ bot | RAG + Memory + Structured Output |
| Research or web-search assistant | Tools + Agents |
| Data extraction pipeline | Structured Output + LCEL |
| Study assistant / quiz generator | Prompts + Structured Output + Memory |

### Where does new code belong?

```text
Learning or experimenting with a concept?    → modules/
A reusable implementation of a pattern?     → recipes/
A complete application?                      → projects/
Genuinely shared infrastructure?             → core/
Unclear?                                     → stop and clarify its responsibility
```

### Dependency direction

A useful **default** is:

```text
projects ──► recipes ──► modules ──► core
```

This is a design guideline, not a reason to hide learning concepts behind abstractions.

- Higher-level application code may reuse lower-level code where that improves clarity.
- A project must not depend on another project.
- Learning modules should remain as independent as practical.
- A module may intentionally duplicate a small amount of setup if moving it into `core/` would hide the concept.
- Do not force every module to depend on `core/`.

> **Reuse when it improves clarity; don't abstract merely to eliminate duplication.**

---

## 🔄 How Code Moves Through the Repo

```text
Learn concept → modules/ → experiment → understand
                                │
                  Worth polishing into a drop-in pattern?
                       │                      │
                      NO                     YES
                       │                      │
              stays in modules/           recipes/
              (still usable)                  │
                       └──────────┬───────────┘
                                  ▼
                  projects/ can use either one
```

Both modules and recipes are reusable. The question at this step is not "is it reusable?" but **"is it worth polishing into a drop-in pattern?"**

**A pattern becomes a recipe when** it solves a common problem · will be needed again and again · the concept is already understood · it is stable enough to document · it can be adapted without rewriting.

Example journey: `modules/06_rag/` → *experiments* → `recipes/basic_rag/` → `projects/` (any project that needs RAG)

Not every module needs a recipe; not every recipe needs a project. Grow by usefulness.

---

## 📝 Documentation Templates

Every module, recipe, and project has its own `README.md` so each is understandable on its own.

### Module `README.md`

```text
# <Concept>
1. What it is
2. Problem it solves & why the problem exists
3. 🎯 Same Task — exact input + expected behavior
4. 🐍 Without LangChain — simplest meaningful baseline
5. 🦜 With LangChain — same task, same input
6. 🔍 What Changed? — abstraction / composition / integration
7. ⚖️ Trade-offs — gains, costs, and limitations
8. Key concepts / vocabulary
9. Minimal working example
10. Experiments (what I changed/broke, and what I learned)
11. Pitfalls & limitations
12. When to use / when simpler code is enough
13. Related concepts & links
```

> **Important:** The baseline does **not** need its own Python file. For small concepts such as prompts or messages, a short code snippet in the README is enough. Create a separate baseline file only when running or modifying the baseline is genuinely useful.

> **Same-task rule:** the baseline and LangChain versions should solve the **same problem with the same meaningful input**. The comparison should show what the abstraction changes, not compare two unrelated demos.

### Recipe `README.md`

```text
# <Recipe name>
- What it does / problem it solves
- When to use (and when not to)
- Dependencies & configuration (env vars)
- How to run
- Expected input → output (with an example)
- How to modify/extend
- Known limitations
```

### Project `README.md`

```text
# <Project name>
- What it does & why it was built
- Features
- Architecture (diagram)
- Tech stack
- LangChain components used (and which recipes/modules they came from)
- How to run
- Key design decisions & trade-offs
```

### Root README vs. Module README

The root README is the **map and operating manual** for the repository. It should explain:

- repository philosophy
- learning roadmap
- architecture and folder responsibilities
- conceptual relationships
- decision guides
- long-term workflow

A module README is the **deep-dive for one concept**. It can contain:

- detailed explanations
- baseline vs. LangChain implementations of the **same task**
- provider/API-specific code
- experiments and failures
- debugging notes
- pitfalls
- exercises
- version-specific details

This keeps the root README useful as the entry point without turning it into the full tutorial for every topic.

---

## 🧪 Learning Method & Progress

> [!IMPORTANT]
> **Experimentation is part of learning.** Change things, break things intentionally, inspect the result, and record what you learned.

### Don't use LangChain just because you can

Sometimes the clearest solution is:

- plain Python
- a provider's SDK
- a small custom abstraction

LangChain becomes useful when its abstractions, integrations, composition model, or higher-level capabilities meaningfully reduce complexity or improve maintainability for the problem at hand.

This repository deliberately compares alternatives so that **using LangChain is a considered engineering choice, not a requirement**.

### The 10-step loop for each concept

```text
 1. Define one concrete task
 2. Solve that exact task without LangChain
 3. Inspect what is manual / repetitive / provider-specific
 4. Learn the LangChain abstraction
 5. Solve the exact same task with LangChain
 6. Compare the two implementations directly
 7. Modify and break both on purpose
 8. Record trade-offs and limitations
 9. Keep reusable code where it naturally belongs
10. Polish a recipe only when the pattern is stable and useful
```

### Experiments (what to try in every module)

- Remove the LangChain component. What manual work comes back?
- Change one input or parameter. Do both implementations still behave the same way?
- Swap the model/provider where the abstraction claims to help. What code actually changes?
- Feed invalid input or unexpected model output. Which side fails, and where?
- Which implementation is easier to debug for this specific task?
- Which abstraction becomes more valuable as the task gains another step?

Experiments are for understanding, not production readiness.

### Definition of "learned"

A topic is learned when I can: explain the concept and the problem it solves · build a basic version · modify it · debug common issues · explain when it's useful **and** when something simpler is enough · use it inside a small app.

### Progress tracker

| Fundamentals | Application Patterns |
|---|---|
| ⬜ 01 Models | ⬜ 06 RAG |
| ⬜ 02 Messages | ⬜ 07 Memory |
| ⬜ 03 Prompts | ⬜ 08 Tools |
| ⬜ 04 Runnables / LCEL | ⬜ 09 Agents |
| ⬜ 05 Structured Output | — |

---

## 🌐 Scope & LangGraph

> [!NOTE]
> LangGraph is intentionally a **separate repository**. This repo only explains the relationship where it helps understand current LangChain behavior.

**In scope:** LangChain fundamentals → models, messages, prompts, runnables, structured output, RAG, memory, tools, agents → recipes → LangChain projects.

**Out of primary scope:** LangGraph implementations/projects · full MLOps · every provider · every vector database · full production infrastructure.

This repository may **explain** LangGraph when that context is necessary to understand current LangChain behavior, but it does not become a LangGraph tutorial or implementation repository.

### LangChain vs. LangGraph

```text
LangChain  → building blocks: models, prompts, tools, retrievers, a ready-made agent
LangGraph  → explicit stateful workflows: custom loops, branching, persistence, human-in-the-loop
```

LangGraph gets its **own repository**. It is a natural next step once LangChain agents feel limiting (custom control flow, complex state, long-running or resumable workflows).

> **Practical overlap:** in LangChain v1, `create_agent` runs on LangGraph, and conversation persistence uses LangGraph's checkpointer. In this repo, these are *used as consumers* in `07_memory` and `09_agents` — without building custom graphs. Anything beyond that belongs in the LangGraph repo.

---

## 📚 Glossary

| Term | Meaning |
|---|---|
| **LLM / Chat model** | Model that takes messages and returns a message. |
| **Stateless** | The model remembers nothing between calls; you resend context. |
| **Token** | Unit of text a model processes; cost and context limits are measured in tokens. |
| **Context window** | Max tokens a model can consider in one call (input + output). |
| **Prompt template** | Reusable prompt with `{variables}`. |
| **Runnable** | Any component with `invoke/stream/batch`; building block of LCEL. |
| **LCEL** | LangChain Expression Language — composing Runnables with `\|`. |
| **Output parser** | Converts model output into a usable type (string, object). |
| **Structured output** | Model response constrained to a schema. |
| **Embedding** | Vector representing the meaning of text; similar meaning → nearby vectors. |
| **Vector store** | Database that stores embeddings and finds the nearest ones. |
| **Retriever** | Component that returns relevant documents for a query. |
| **Chunk** | Piece of a document after splitting. |
| **RAG** | Retrieve relevant data, then generate an answer using it. |
| **Tool** | Function the model can request to be called. |
| **Tool call** | The model's structured request: tool name + arguments. |
| **Agent** | Loop where the model chooses tools until the task is done. |
| **Thread** | One conversation's isolated state, identified by an ID. |
| **Checkpointer** | Component that saves conversation/agent state between calls. |
| **Hallucination** | Fluent but incorrect or unsupported model output. |

---

## 🔗 References

- Official docs: <https://docs.langchain.com>
- LangChain v1 migration guide (see "Version note" above): <https://docs.langchain.com/oss/python/migrate/langchain-v1>
- API reference: <https://reference.langchain.com/python>

> When a module's code conflicts with a tutorial, trust the official docs for the version pinned in that module.

---

## ⭐ Core Principle

> **Learn it → Build it → Experiment with it → Understand it → Document it → Reuse it.**

---

### 🧪 Learn it. Break it. Understand it. Reuse it.

**LangChain Lab** — a growing personal knowledge base for building LLM applications.

