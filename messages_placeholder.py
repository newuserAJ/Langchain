from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# -----------------------------
# Load chat history from file
# -----------------------------
chat_history = []

with open("chat_history.txt") as f:
    for line in f:
        msg_type, rest = line.strip().split("(", 1)
        content = rest.split('content="', 1)[1].rsplit('"', 1)[0]

        if msg_type == "HumanMessage":
            chat_history.append(HumanMessage(content=content))
        else:
            chat_history.append(AIMessage(content=content))

# -----------------------------
# Chat prompt template
# -----------------------------
chat_template = ChatPromptTemplate([
    ("system", "You are a customer support assistant"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

# -----------------------------
# Invoke prompt
# -----------------------------
prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "Where is my refund?"
})

print(prompt)
