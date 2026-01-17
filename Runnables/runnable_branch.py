from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnableBranch,RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGroq(model='llama-3.1-8b-instant', temperature=0)
parser=StrOutputParser()
prompt1=PromptTemplate(template='write a detailed report on {topic}',input_variables=['topic'])

prompt2=PromptTemplate(template="summarize  the following {text}",input_variables=['text'])

report_gen=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch((lambda x:len(x.split())>500,RunnableSequence(prompt2,model,parser)),
                            RunnablePassthrough())

final_chain=RunnableSequence(report_gen,branch_chain)
print(final_chain.invoke({'topic':' cricket'}))


