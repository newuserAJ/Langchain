from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(model='llama-3.1-8b-instant', temperature=0)
prompt=PromptTemplate(template='give a detailed analysis of the following webpage content:\n {document}',input_variables=['document'])
parser=StrOutputParser()
url='https://github.com/newuserAJ'
loader=WebBaseLoader(url)

docs=loader.load()

chain=prompt|model|parser

print(chain.invoke({'document':docs[0].page_content}))