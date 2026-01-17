from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGroq(model="llama-3.1-8b-instant", temperature=0)

prompt=PromptTemplate(template='',input_variables=[''])



