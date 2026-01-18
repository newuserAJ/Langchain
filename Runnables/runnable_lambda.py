#RunnablePassthrough allows user to print put input as output along with other outputs
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def word_count(text:str)->int:
    return len(text.split())
llm=ChatGroq(model="llama-3.1-8b-instant", temperature=0)

prompt=PromptTemplate(template='write a joke about {topic}',input_variables=['topic'])

parser=StrOutputParser()

joke_chain=RunnableSequence(prompt,llm,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
})

final_chain=RunnableSequence(joke_chain,parallel_chain)

result=final_chain.invoke('people')

final_result= '''{} \n word count:{}'''.format(result['joke'],result['word_count'])

print(final_result)

