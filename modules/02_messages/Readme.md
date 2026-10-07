# 💬 Module 02 — Messages

> **Goal:** Understand how LangChain represents conversational information using typed message objects and why messages are a foundation for chat models, memory, tool calling, and agents.

---

## 🎯 What You Should Learn

By the end of this module, you should be able to explain and use:

- `SystemMessage`
- `HumanMessage`
- `AIMessage`
- `ToolMessage`
- message content
- message order
- conversation history
- invoking a chat model with a list of messages
- inspecting message objects and their important fields

The target is not to memorize class names.

The target is to understand:

> **What information does a message carry, why does the role matter, and why is a structured message better than treating a conversation as one large string?**

---

# 🧠 1. Why Messages Exist

A chat model does not only receive "text".

A conversation contains information about **who said something**.

For example:

```text
System: You are a CSE tutor.
Human: Explain recursion.
AI: Recursion is...
Human: Give me an example in C.
```

The model needs to know which content is an instruction, which content is user input, and which content came from the model.

This is why LangChain provides structured message types.

---

# 🧩 2. Core Message Types

| Message Type | Represents | Main Purpose |
|---|---|---|
| `SystemMessage` | System instructions | Defines behavior, rules, or context |
| `HumanMessage` | User input | Represents the user's message |
| `AIMessage` | Model output | Represents the model's response |
| `ToolMessage` | Tool result | Represents the result returned by a tool |

### Important idea

A message is more than just text.

It can carry structured information such as:

- role/type
- content
- metadata
- identifiers
- tool-call information
- usage/provider information, depending on the provider and response

---

# 🔬 3. Same Task

For this module, use **one consistent task** while learning the concept.

### 🎯 Task

Build a small CSE tutor interaction.

The conversation should contain:

```text
System → defines the tutor behavior
Human  → asks a CSE question
AI     → model response
Human  → asks a follow-up
```

Use LangChain message objects to represent the conversation.

### Example scenario

```text
System:
You are a concise CSE tutor.

Human:
What is recursion?

AI:
<model response>

Human:
Give me a simple example.
```

Do not copy the example response manually. Let the model generate it.

---

# 🦜 4. LangChain Implementation

Your first implementation should focus only on LangChain.

You should discover yourself:

1. Where the message classes are imported from.
2. How to create each message.
3. How multiple messages are passed to a chat model.
4. What type of object the model returns.
5. How the returned `AIMessage` differs from the messages you created.

Keep the implementation small.

The goal is understanding, not building an application.

---

# 🔍 5. Inspect the Messages

After getting the conversation working, inspect the objects.

For your created messages, investigate:

- their Python type
- their content
- their important attributes

For the returned `AIMessage`, investigate:

- `content`
- `response_metadata`
- `usage_metadata`
- `tool_calls` when available
- any other useful fields you discover

> **Do not assume every field will appear for every provider/model.**
> Provider integrations can expose different metadata and capabilities.

---

# 🧪 6. Experiments

Once the basic message flow works, start changing one thing at a time.

### Experiment A — Change the System Message

Change the system instruction.

Observe how the model response changes.

Question:

> What influence does `SystemMessage` have compared with `HumanMessage`?

---

### Experiment B — Change Message Order

Try changing the order of the messages.

Observe what happens.

Question:

> Why can message order matter in a conversation?

---

### Experiment C — Add More Conversation History

Create a longer sequence:

```text
System
Human
AI
Human
AI
Human
```

Observe how the model uses the previous messages as context.

Question:

> Is the model itself remembering the conversation, or are we providing the previous messages again?

---

### Experiment D — Inspect `AIMessage`

Take the response returned by the model and inspect it carefully.

Compare it with the `HumanMessage` objects you created.

Question:

> Why does the model return an `AIMessage` instead of an ordinary string?

---

# 🛠️ 7. Message Content

Explore what `content` contains.

For a normal text response, it may look like a string.

Depending on the provider and features being used, content may also be represented using structured content blocks.

Your job is to observe this rather than assuming:

```text
content == always a string
```

Record what your current provider/model actually returns.

---

# 🔧 8. ToolMessage Preview

Do not build tools yet.

That belongs to **Module 08 — Tools**.

For now, only understand the role of `ToolMessage`.

Conceptually:

```text
Human
   ↓
AIMessage with tool call
   ↓
Tool executes
   ↓
ToolMessage with result
   ↓
Model continues
```

The important idea is:

> `ToolMessage` represents the result of a tool execution that is returned to the model as part of the conversation context.

You will implement this properly later.

---

# ⚖️ 9. What LangChain Gives You

At this stage, focus on the practical value of structured messages.

LangChain gives you a common message representation that can be used across supported chat-model integrations.

This helps the application reason about conversations in terms of **message objects and roles**, instead of manually maintaining provider-specific message representations everywhere.

Do not treat this as "LangChain magically manages the conversation."

You are still responsible for:

- what messages exist
- what order they are in
- what history you provide
- what information you send to the model

---

# 🚧 10. Common Pitfalls

### ❌ Treating every response as a string

The model response is an `AIMessage`.

Inspect it before extracting only the text.

### ❌ Ignoring message order

Conversation order can affect what the model sees as context.

### ❌ Mixing message roles incorrectly

A system instruction, user request, model response, and tool result have different meanings.

### ❌ Assuming metadata is identical across providers

Metadata varies depending on the provider, model, and features.

### ❌ Building memory here

Message history is the foundation for conversation state, but **memory as an application pattern** is covered in Module 07.

---

# 🧠 11. Questions You Must Be Able to Answer

Before leaving this module, you should be able to answer these without looking them up:

1. What is a message in LangChain?
2. Why are roles important?
3. What is the purpose of `SystemMessage`?
4. What is the purpose of `HumanMessage`?
5. What is an `AIMessage`?
6. What is a `ToolMessage`?
7. Why doesn't a chat model simply receive one long string?
8. What happens when a list of messages is passed to `model.invoke()`?
9. Why does message order matter?
10. Is an `AIMessage` the same thing as its `content`?
11. What kind of information can an `AIMessage` contain besides text?
12. Is message history the same thing as long-term application memory?

---

# 🧪 12. Learning Record

After completing each experiment, record:

```text
Experiment:
What I changed:
What happened:
Why I think it happened:
What I learned:
```

This repository is meant to capture **your understanding**, including mistakes and discoveries.

---

# 📁 13. Suggested Module Structure

Start small.

```text
02_messages/
├── README.md
└── <your experiment file>
```

Do not create multiple files just because the module has multiple tasks.

Create another file only when an experiment becomes large enough or conceptually separate enough to deserve one.

---

# ✅ Completion Checklist

You can consider this module complete when you can:

- [ ] create `SystemMessage`
- [ ] create `HumanMessage`
- [ ] understand `AIMessage`
- [ ] explain the role of `ToolMessage`
- [ ] send a list of messages to a chat model
- [ ] inspect the returned `AIMessage`
- [ ] explain the importance of message order
- [ ] explain why messages are better than an unstructured conversation string
- [ ] run at least 2 meaningful experiments
- [ ] explain the concept without relying on copied code

---

# 🔗 Related Modules

```text
01 Models
   ↓
02 Messages
   ↓
03 Prompts
   ↓
04 Runnables
```

Messages are also foundational to:

```text
07 Memory
08 Tools
09 Agents
```

---

# 📚 References

Use the official LangChain documentation as the source of truth for current APIs and provider-specific behavior.

Recommended topics to read:

- LangChain Messages
- Chat model invocation
- `AIMessage`
- `ToolMessage`
- Message content and content blocks

> **Learning rule:** Read enough to understand the concept, then implement it yourself. Do not copy a complete tutorial into the repository.
