from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Groq model
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7
)

# Initialize chat history
chat_history = [SystemMessage(content="You are a assistant")]
print("Chat started! Type 'exit' to quit.")

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    result = model.invoke(chat_history)
    print("AI:", result.content)
    chat_history.append(AIMessage(content=result.content))
print("Chat ended.")
print(chat_history)