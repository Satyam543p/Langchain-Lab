# Module 04 --- Chains

## 🎯 Goal

Understand how LangChain connects multiple components into a workflow
where the output of one step becomes the input of another.

This module focuses on practical chain patterns rather than memorizing
APIs.

------------------------------------------------------------------------

## 🧠 Core Idea

A chain is a sequence or combination of LangChain components connected
to perform a task.

``` text
Input
  ↓
Component
  ↓
Component
  ↓
Output
```

LangChain's pipe operator makes composition easy:

``` python
chain = prompt | model
```

Then the complete workflow can be executed with:

``` python
chain.invoke(input)
```

------------------------------------------------------------------------

## 1. Simple Chain

**File:** `01_simple_chain.py`

### Pattern

``` text
Prompt → Model
```

Example:

``` python
chain = prompt | model
```

### What this teaches

-   Basic chain composition
-   The `|` operator
-   Invoking a complete workflow with `.invoke()`
-   Passing data between components

------------------------------------------------------------------------

## 2. Sequential Chain

**File:** `02_sequential_chain.py`

### Pattern

``` text
Prompt 1
   ↓
Model
   ↓
Parser
   ↓
Prompt 2
   ↓
Model
   ↓
Parser
```

Example:

``` python
chain = prompt1 | model | parser | prompt2 | model | parser
```

The output of each step becomes the input of the next step.

### Example workflow

``` text
Topic
 ↓
Generate detailed report
 ↓
Convert response to text
 ↓
Generate summary
 ↓
Convert response to text
 ↓
Final summary
```

A sequential chain can involve multiple model calls, so provider limits
such as token limits can affect individual steps.

------------------------------------------------------------------------

## 3. Parallel Chain

**File:** `03_parallel_chain.py`

### Pattern

``` text
             ┌──→ Chain A ──→ Result A
Input ───────┤
             └──→ Chain B ──→ Result B
```

Multiple independent operations can work from the same input.

### What this teaches

-   Parallel execution
-   Multiple branches from the same input
-   Combining independent results
-   Difference between sequential and parallel workflows

------------------------------------------------------------------------

## 4. Conditional Chain

**File:** `04_conditional_chain.py`

### Pattern

``` text
Input
  ↓
Classifier
  ↓
Condition
 ┌───────────────┐
 ↓               ↓
Positive       Negative
 ↓               ↓
Prompt 2       Prompt 3
```

The route taken depends on the result of an earlier step.

The experiment uses:

-   `RunnableBranch`
-   `RunnableLambda`
-   `PydanticOutputParser`
-   `StrOutputParser`
-   Pydantic models
-   Conditional routing

### Example

``` text
"Lovely"
   ↓
Sentiment classifier
   ↓
positive
   ↓
Positive-response prompt
   ↓
Final response
```

------------------------------------------------------------------------

## 🔄 Data Flow Matters

One of the most important lessons from conditional chains is
understanding what each component actually receives.

For example:

``` text
Model
 ↓
StrOutputParser
 ↓
"positive"
```

The next component receives a string.

With structured output:

``` text
Model
 ↓
PydanticOutputParser
 ↓
Text(
    text="Lovely",
    sentiment="positive"
)
```

the next runnable receives a structured Pydantic object.

The next runnable must therefore expect the type and structure produced
by the previous runnable.

------------------------------------------------------------------------

## 🧩 Parsers in Chains

### `StrOutputParser`

Converts an LLM response into plain text.

``` text
AIMessage
   ↓
StrOutputParser
   ↓
string
```

Useful when the next prompt expects normal text.

### `PydanticOutputParser`

Converts structured model output into a Pydantic object.

``` text
LLM response
   ↓
PydanticOutputParser
   ↓
Pydantic object
```

Useful when later steps need reliable structured fields.

------------------------------------------------------------------------

## ⚠️ Important Lessons

### 1. Components must agree on data shape

If one step produces:

``` python
"positive"
```

the next step cannot assume it received:

``` python
{"sentiment": "positive"}
```

### 2. Preserve information when later steps need it

If a classifier consumes the original text and only returns the
sentiment, the original text is no longer available downstream unless it
is explicitly preserved.

### 3. Provider limitations can affect chains

A chain may be logically correct but still fail because an LLM provider
rejects a request due to model availability, rate limits, or token
limits.

### 4. Different outputs require different parsers

Don't use a Pydantic parser for a final free-form response simply
because a Pydantic parser was used earlier in the chain.

------------------------------------------------------------------------

## 📁 Module Structure

``` text
04_chains/
├── README.md
├── 01_simple_chain.py
├── 02_sequential_chain.py
├── 03_parallel_chain.py
└── 04_conditional_chain.py
```

------------------------------------------------------------------------

## 🔗 Chains vs Runnables

Chains demonstrate workflow patterns created by connecting components.

Runnables are the lower-level abstraction that makes these compositions
possible.

``` text
Chains
  ↓
Workflow patterns
  ↓
Built using Runnable concepts
```

The next module goes deeper into **Runnables themselves**.

------------------------------------------------------------------------

## ✅ Completion Checklist

-   [x] Understand basic chain composition
-   [x] Use the `|` operator
-   [x] Build a sequential workflow
-   [x] Build a parallel workflow
-   [x] Build a conditional workflow
-   [x] Understand data flow between chain steps
-   [x] Use `StrOutputParser`
-   [x] Use `PydanticOutputParser`
-   [x] Understand structured vs plain-text outputs
-   [x] Understand that chains can contain multiple model calls
-   [x] Understand provider limitations can affect execution

------------------------------------------------------------------------

## 🧠 Mental Model

> **A Chain is a workflow created by connecting LangChain components so
> that data flows from one step to another.**

The important skill is not memorizing chain classes.

It is understanding:

``` text
What is the input?
        ↓
What does this component produce?
        ↓
What does the next component expect?
        ↓
How should the data be routed?
```

That data-flow understanding becomes the foundation for the
**Runnables** module.
