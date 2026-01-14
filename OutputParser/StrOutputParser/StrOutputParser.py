from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2
)
model1=llm

#1st template
template1=PromptTemplate(template="write a detailed report on {topic}",input_variables=['topic'])

#2nd template
template2=PromptTemplate(template="write a 5 point summary on the following text.\n {text}",input_variables=['text'])


prompt1=template1.invoke({'topic':'blackholes'})
result=model1.invoke(prompt1)

prompt2=template2.invoke({'text':result.content})
result1=model1.invoke(prompt2)

print(result1.content)


