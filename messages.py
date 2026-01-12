from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model=ChatGroq(model="llama-3.3-70b-versatile",temperature=0.7)

messages=[SystemMessage(content="You are a assistant"),
          HumanMessage(content="What is the capital of USA?")]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)
