from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatGroq(model='llama-3.1-8b-instant', temperature=0)
parser=StrOutputParser()
prompt=PromptTemplate(template='give a detailed analysis of the following document:\n {document}',input_variables=['document'])

loaderr=TextLoader('cricket.txt',encoding='utf-8')

docs=loaderr.load()
print(docs[0])

chain=prompt|model|parser

print(chain.invoke({'document':docs[0].page_content}))