from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv()

model=ChatGroq(model="llama-3.1-8b-instant", temperature=0)

prompt=PromptTemplate(template='Tell me a fun fact about {topic}',input_variables=['topic'])