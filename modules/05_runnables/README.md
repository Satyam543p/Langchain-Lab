# Module 05 — Runnables

## 🎯 Goal

Understand **why LangChain introduced Runnables**, how they make components work consistently, and how to compose those components into workflows.

This module builds on **Module 04 — Chains**. Chains helped us build workflows; Runnables help explain the common interface and reusable building blocks behind those workflows.

---

## 1. The Problem Runnables Help Solve

Imagine building an AI workflow that:

1. Formats a prompt.
2. Sends it to a language model.
3. Converts the model response into text.
4. Passes that text into another prompt.

```text
Input → Prompt → Model → Parser → Prompt → Model → Output
```

Each component has a different responsibility. Without a consistent way to execute and connect them, you may have to call each component separately, pass intermediate results manually, and write extra glue code as workflows grow.

For example, a manually coordinated workflow could look like:

```python
formatted_prompt = prompt.format(topic="Science")
model_result = model.invoke(formatted_prompt)
plain_text = parser.invoke(model_result)
```

This works, but you must coordinate the order, inputs, intermediate outputs, and data types yourself.

Earlier LangChain APIs also included specialized chain classes for particular patterns, such as `LLMChain` and `SequentialChain`. These were useful, but learning and connecting different specialized classes could make composition feel fragmented.

**Runnables provide a more consistent composition model:** components that implement the Runnable interface can be executed and connected using common patterns. This does not mean every older chain class was bad or that Runnables remove every integration detail. The key benefit is a shared interface for execution and composition.

---

## 2. What Is a Runnable?

A Runnable accepts an input, performs an operation, and returns an output.

A common execution method is:

```python
result = runnable.invoke(input)
```

The input and output depend on the specific Runnable:

| Runnable | Example input | Example output |
|---|---|---|
| `PromptTemplate` | `{"topic": "Science"}` | A formatted prompt value |
| Chat model | A prompt or messages | An `AIMessage` |
| `StrOutputParser` | An `AIMessage` | A string |
| `RunnableLambda` | Whatever its function accepts | Whatever its function returns |
| `RunnablePassthrough` | Any input | The same input |

The common interface does **not** mean every Runnable accepts the same data type. It means they share a consistent execution/composition model, provided each connected step can accept the previous step's output.

---

## 3. Types of Runnables: Primitive and Composite

For learning purposes, it is useful to distinguish between **individual Runnable building blocks** and **composed Runnables**. These are explanatory categories, not a strict official Python class hierarchy.

### A. Primitive / individual Runnable building blocks

These perform one focused operation or adapt an existing component/function to the Runnable interface.

| Runnable | What it does |
|---|---|
| `RunnableLambda` | Wraps a Python function as a Runnable |
| `RunnablePassthrough` | Returns the input unchanged |
| `PromptTemplate` | Formats input variables into a prompt |
| Chat model | Sends input to an LLM and returns a response |
| Output parser | Converts a model response into a desired format |

Example: wrapping a Python function.

```python
from langchain_core.runnables import RunnableLambda

def square(x):
    return x ** 2

square_runnable = RunnableLambda(square)
print(square_runnable.invoke(5))  # 25
```

`RunnableLambda` does not decide how to compose a whole workflow. It makes your function usable as a Runnable component.

### B. Composite / composed Runnables

These combine other Runnables to form a larger workflow.

| Runnable | What it does |
|---|---|
| `RunnableSequence` | Executes steps in order |
| `RunnableParallel` | Sends the same input to multiple branches and collects results |
| `RunnableBranch` | Selects a branch based on ordered conditions |

Example: combining two individual Runnables.

```python
from langchain_core.runnables import RunnableLambda, RunnableSequence

double = RunnableLambda(lambda x: x * 2)
square = RunnableLambda(lambda x: x ** 2)

chain = RunnableSequence(double, square)
print(chain.invoke(5))  # 100
```

The result is `100` because the first Runnable returns `10`, which becomes the input to the second Runnable.

**Remember:** `RunnableLambda` is an individual building block; `RunnableSequence`, `RunnableParallel`, and `RunnableBranch` compose Runnables. `RunnablePassthrough` is another individual building block that is especially useful inside composed workflows.

---

## 4. Why Composition Matters

Once components implement the Runnable interface, they can be connected using the pipe operator (`|`).

```python
chain = prompt | model | parser
result = chain.invoke({"topic": "Science"})
```

Conceptually:

```text
{"topic": "Science"}
        ↓
      Prompt
        ↓ formatted prompt
       Model
        ↓ AIMessage
      Parser
        ↓ string
      Result
```

You invoke the complete workflow once instead of manually invoking every step.

You can also construct a sequence explicitly:

```python
chain = RunnableSequence(prompt, model, parser)
```

For the steps to connect successfully, each component must be able to accept the previous component's output.

---

## 5. Runnable Concepts and Visual Workflows

Each experiment focuses on a concept. The diagrams below show the **purpose and data flow**; open the linked Python file to see the implementation.

### 5.1 Runnable basics — `RunnableLambda`

**What:** `RunnableLambda` adapts a normal Python function so it can be invoked and composed like other Runnables.

**Why:** It lets you add your own transformation to a LangChain workflow.

**Visual workflow** — `01_runnables_basic.py`

```text
Input: 5
   ↓
RunnableLambda(double)
   ↓ 10
RunnableLambda(square)
   ↓
Output: 100
```

The file also invokes a `PromptTemplate` directly and inspects its output type.

### 5.2 RunnableSequence — ordered execution

**What:** `RunnableSequence` runs steps in order. Each step receives the previous step's output.

**Why:** Use it when a task has dependent stages, such as generating a report and then summarizing it.

**Visual workflow** — `02_runnable_sequence.py`

```text
Input: topic
   ↓
Report Prompt
   ↓
Chat Model
   ↓
String Output Parser
   ↓
Summary Prompt
   ↓
Chat Model
   ↓
String Output Parser
   ↓
Final summary
```

**LLM-based sequence** — `02_runnable_sequenceLLM.py`

Use this file for the sequence experiment that connects prompts, an LLM, and parsers in a real model workflow.

### 5.3 RunnablePassthrough — preserve the input

**What:** `RunnablePassthrough` returns its input unchanged.

**Why:** A later step may need the original input even when another branch transforms it.

**Visual workflow** — `03_runnable_passthrough.py`

```text
Input: {"text": "lovely"}
             |
       ┌─────┴─────┐
       ↓           ↓
  Transform     Passthrough
       ↓           ↓
  "LOVELY"   {"text": "lovely"}
       └─────┬─────┘
             ↓
       Combined result
```

This experiment pairs the passthrough with a transformation inside `RunnableParallel`, so you can compare the transformed value with the preserved input.

### 5.4 RunnableParallel — independent branches

**What:** `RunnableParallel` sends the same input to multiple Runnable branches and collects their outputs in a dictionary.

**Why:** Use it when multiple independent operations need the same input. It is different from a sequence: branches do not wait for one another's outputs.

**Visual workflow** — `04_RunnableParallel.py`

```text
                 Input
                   |
           RunnableParallel
             /           \
            ↓             ↓
      Branch A         Branch B
      Transform        Preserve
            ↓             ↓
        Result A       Result B
             \           /
              ↓         ↓
           Combined dictionary
```

### 5.5 RunnableBranch — conditional routing

**What:** `RunnableBranch` checks conditions in order and executes the first matching branch. If none matches, it executes the default branch.

**Why:** Use it when the next operation depends on the input or on a classification result.

**Visual workflow** — `05_Runnable_Branch.py`

```text
Input: {"num": 5}
        ↓
RunnableLambda: check number
        ↓
 Boolean result
        ↓
   RunnableBranch
     /    |     \
  True   False  Default
    ↓      ↓       ↓
 Positive Negative Fallback
```

In this experiment, the checker returns a Boolean, so the branch conditions must test that Boolean—not the original dictionary. Ensure the labels match the logic: `num > 0` distinguishes positive from non-positive, so zero should not be labelled negative.

---

## 10. `invoke()` vs `batch()` vs `stream()`

These methods are different ways to execute a Runnable. They do not change the Runnable's core job; they change how you supply inputs or receive outputs.

| Method | Best for | Input shape | Result behavior |
|---|---|---|---|
| `.invoke(input)` | One input | A single input value | Returns one completed result |
| `.batch(inputs)` | Multiple independent inputs | A list of inputs | Returns a list of results |
| `.stream(input)` | Receiving output progressively | A single input value | Yields chunks as they become available, if supported |

### `invoke()` — one input, one result

```python
from langchain_core.runnables import RunnableLambda

double = RunnableLambda(lambda x: x * 2)

result = double.invoke(5)
print(result)  # 10
```

Use this for a single input when you want the completed result.

### `batch()` — several inputs, a list of results

```python
from langchain_core.runnables import RunnableLambda

double = RunnableLambda(lambda x: x * 2)

results = double.batch([1, 2, 3, 4])
print(results)  # [2, 4, 6, 8]
```

Use this when you want to process multiple inputs with the same Runnable. Actual parallelism and performance depend on the Runnable and its configuration; `.batch()` is the batch interface, not a guarantee that every operation runs simultaneously.

### `stream()` — receive chunks progressively

```python
from langchain_core.runnables import RunnableLambda

def count_up_to(n):
    for number in range(1, n + 1):
        yield number

counter = RunnableLambda(count_up_to)

for chunk in counter.stream(3):
    print(chunk)
```

For this generator-based Runnable, the output is yielded progressively:

```text
1
2
3
```

For an LLM, streaming commonly means receiving pieces of generated text before the full response is complete. Exact behavior depends on the Runnable and whether its components support streaming; a Runnable that returns one ordinary value may not provide meaningful incremental output.

### Quick rule

- Need one completed result? Use `invoke()`.
- Need results for multiple inputs? Use `batch()`.
- Need output progressively as it is produced? Use `stream()`.

---

## 11. Data Flow: The Most Important Skill

The common interface makes composition possible, but it does **not** eliminate the need to understand data.

Before connecting two steps, ask:

1. What input does this Runnable receive?
2. What type and structure does it return?
3. What does the next Runnable expect?
4. Do I need to preserve information for a later step?

Example:

```text
{"text": "lovely"}
       ↓
RunnableParallel
       ↓
{
    "upper": "LOVELY",
    "original": {"text": "lovely"}
}
```

`RunnablePassthrough` preserves the complete input dictionary. `RunnableLambda` extracts and transforms a field. `RunnableParallel` collects both results.

This is the same kind of data-flow reasoning you practised in the conditional-chain experiment.

---

## 12. Chains vs Runnables

- **Chains** focus on workflow patterns, such as simple, sequential, parallel, and conditional workflows.
- **Runnables** provide the common interface and composable building blocks used to create those workflows.

They are not competing concepts. A chain can be built by composing Runnables. Your Chains module focuses on workflow patterns; this module focuses on the pieces and execution model that make composition possible.

---

## ✅ Completion Checklist

- [x] Invoke a `PromptTemplate` directly
- [x] Wrap Python functions with `RunnableLambda`
- [x] Compose Runnables with `|`
- [x] Build a sequence with `RunnableSequence`
- [x] Pass input through with `RunnablePassthrough`
- [x] Collect results with `RunnableParallel`
- [x] Route inputs with `RunnableBranch`
- [x] Understand data types and structures between steps
- [ ] Practise `.batch()` with multiple inputs
- [ ] Practise `.stream()` with a streaming-capable Runnable

---

## 🧠 Mental Model

> **Runnables give LangChain components a consistent way to execute and compose. Individual Runnables perform focused operations; composite Runnables connect those operations into larger workflows.**

The key is understanding both the shared interface and the data that flows between components.
