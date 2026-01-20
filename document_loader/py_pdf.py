from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatGroq(model='llama-3.1-8b-instant', temperature=0)
parser=StrOutputParser()
prompt=PromptTemplate(template='give a detailed analysis of the following document:\n {document}',input_variables=['document'])

loaderr=PyPDFLoader('dl-curriculum.pdf')
docs=loaderr.load()
print(len(docs))  # Print number of pages loaded
print(docs[0].page_content)  #Print  content of the first page