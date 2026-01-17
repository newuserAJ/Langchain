#RunnablePassthrough allows user to print put input as output along with other outputs
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm=ChatGroq(model="llama-3.1-8b-instant", temperature=0)

prompt=PromptTemplate(template='write a joke about {topic}',input_variables=['topic'])

prompt2=PromptTemplate(template='Explain the joke {text}',input_variables=['text'])
parser=StrOutputParser()

joke_chain=RunnableSequence(prompt,llm,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,llm,parser)
})

final_chain=RunnableSequence(joke_chain,parallel_chain)

print(final_chain.invoke('cricket'))

