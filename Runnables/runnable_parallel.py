from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableSequence
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

parser=StrOutputParser()

llm=ChatGroq(model="llama-3.1-8b-instant", temperature=0)

prompt=PromptTemplate(template='genrate a tweet {topic}',input_variables=['topic'])

prompt2=PromptTemplate(template='generate a linkedin post about {topic}',input_variables=['topic'])

parallel_chain=RunnableParallel({'tweet':RunnableSequence(prompt,llm,parser),
                                'linkedin':RunnableSequence(prompt2,llm,parser)})

result=parallel_chain.invoke({'topic':'AI'})

print(result['tweet'])
print(result['linkedin'])


    