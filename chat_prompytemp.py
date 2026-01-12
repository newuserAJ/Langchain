from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

chat_template = ChatPromptTemplate([
    ("system","You are a {domain} expert"),
    ("human","Explain the concept of {concept} in simple terms.")
])

prompt=chat_template.invoke({"domain":"cricket","concept":"LBW"})
print(prompt)