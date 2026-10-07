from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    ToolMessage
)

messages = [
    HumanMessage(content="What is 25 × 4?")
]

# Represent an AI message that requested a tool
ai_message = AIMessage(
    content="",
    tool_calls=[
        {
            "name": "calculator",
            "args": {"expression": "25 * 4"},
            "id": "call_123"
        }
    ]
)

messages.append(ai_message)

# Represent the result returned by the tool
tool_message = ToolMessage(
    content="100",
    tool_call_id="call_123"
)

messages.append(tool_message)

for msg in messages:
    print("\nType:", type(msg).__name__)
    print("Content:", msg.content)

    if isinstance(msg, AIMessage):
        print("Tool calls:", msg.tool_calls)

    if isinstance(msg, ToolMessage):
        print("Tool call ID:", msg.tool_call_id)