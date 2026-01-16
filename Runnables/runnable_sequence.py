from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm=ChatGroq(model="llama-3.1-8b-instant", temperature=0)

prompt=PromptTemplate(template='write a joke about {topic}',input_variables=['topic'])

prompt2=PromptTemplate(template='Explain the joke {text}',input_variables=['text'])
parser=StrOutputParser()

chain=RunnableSequence(prompt,llm,parser,prompt2,llm,parser)

print(chain.invoke({'topic':'chickens'}))

