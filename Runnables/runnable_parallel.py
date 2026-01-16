from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

llm=ChatGroq(model="llama-3.1-8b-instant", temperature=0)

prompt=PromptTemplate(template='',input_variables=[])

chain=RunnableParallel()