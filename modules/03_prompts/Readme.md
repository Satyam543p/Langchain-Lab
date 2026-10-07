# 03 — Prompts

> Learn how LangChain helps create reusable, structured, dynamic, and composable prompts.

## Why Prompts?

A prompt defines **what we want the model to do** and the information it should use.

Messages can be created directly:

```python
[
    SystemMessage(content="You are a CSE teacher"),
    HumanMessage(content="Explain pointers")
]
```

This works, but prompt templates make the structure easier to **reuse, parameterize, validate, and compose**.

```text
Prompt Template
      ↓
Fill variables / context
      ↓
Structured Prompt
      ↓
Model
```

### Messages vs Prompt Templates

| Messages | Prompt Templates |
|---|---|
| Represent conversation data | Define reusable prompt structure |
| System / Human / AI / Tool | Support variables and templates |
| Usually constructed directly | Can validate template structure |
| Useful for conversation state | Easy to reuse and compose |
| Content is specified manually | Data can be inserted dynamically |

> **Prompts don't replace messages.** `ChatPromptTemplate` can generate the structured messages sent to the model.

---

## Concepts Covered

### `PromptTemplate`

Reusable text prompts with variables.

```text
Greet {name} in 5 languages.
```

→ `prompt_template.py`

**Key features:**
- Input variables
- Template validation with `validate_template=True`
- Reusable prompt structure
- Composition with other LangChain components

---

### `ChatPromptTemplate`

Creates structured chat prompts using roles such as `system` and `human`.

```text
System → You are a helpful {domain} expert
Human  → Explain {topic}
```

→ `chat_prompt_template.py`

---

### `MessagesPlaceholder`

Provides a dynamic position where existing messages can be inserted.

```text
System
  ↓
{chat_history}
  ↓
Human
```

→ `message_placeholder.py`

The experiment also demonstrates the difference between **actual LangChain message objects** and strings that only contain text such as `HumanMessage(...)`.

---

### Saving & Loading Prompts

Prompts can be saved and loaded for reuse.

```text
PromptTemplate
    ↓ save()
template.json
    ↓ load_prompt()
PromptTemplate
```

→ `prompt_generator.py`  
→ `template.json`

---

### Few-Shot Prompting

Give the model a few examples so it can follow the demonstrated pattern.

```text
Input: happy
Output: positive

Input: angry
Output: negative

Input: excited
Output:
```

LangChain provides `FewShotPromptTemplate` to construct these prompts.

---

## Prompt Composition

Prompt templates can be composed with other LangChain components.

```text
Prompt
  ↓
Model
  ↓
Output
```

For example:

```python
chain = prompt | model
```

This makes the prompt one component of a larger LangChain pipeline.

> The deeper concepts behind `|`, Runnable composition, `invoke()`, streaming, batching, and pipelines are covered in **Module 04 — Runnables**.

---

## Files

```text
03_prompts/
├── README.md
├── prompt_template.py
├── chat_prompt_template.py
├── message_placeholder.py
├── prompt_generator.py
├── template.json
└── chat_history.txt
```

| File | Demonstrates |
|---|---|
| `prompt_template.py` | `PromptTemplate`, variables, validation |
| `chat_prompt_template.py` | `ChatPromptTemplate` |
| `message_placeholder.py` | `MessagesPlaceholder` + chat history |
| `prompt_generator.py` | Saving/loading prompts |
| `template.json` | Saved prompt definition |
| `chat_history.txt` | Example history data |

---

## Mental Model

```text
Prompt
  │
  ├── Instructions
  ├── Variables
  ├── Context / History
  └── Examples
          ↓
   Prompt Template
          ↓
   Structured Prompt
          ↓
        Model
          ↓
      AIMessage
```

---

## Module Boundary

This module focuses on **creating, structuring, validating, reusing, and composing prompts**.

The deeper mechanics of LangChain composition belong to:

**→ Module 04 — Runnables**

---

## Completion Checklist

- [x] `PromptTemplate`
- [x] Input variables
- [x] Template validation
- [x] `ChatPromptTemplate`
- [x] `MessagesPlaceholder`
- [x] Dynamic chat history
- [x] Saving/loading prompts
- [x] Few-shot prompting
- [x] `FewShotPromptTemplate`
- [x] Message vs Prompt
- [x] Prompt composition / chain support
