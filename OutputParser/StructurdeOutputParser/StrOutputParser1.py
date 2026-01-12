from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2
)
model1=llm

#1st template
template1=PromptTemplate(template="write a detailed report on {topic}",input_variables=['topic'])

#2nd template
template2=PromptTemplate(template="write a 5 line summary on the following text.\n {text}",input_variables=['text'])

parser=StrOutputParser()


# we will make chain t1->model1->parser->t2->model1->parser

chain=template1 | model1 | parser | template2 | model1 | parser

result=chain.invoke({'topic':'blackholes'})

print(result)


