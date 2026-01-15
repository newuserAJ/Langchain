from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm=ChatGroq(model="llama-3.1-8b-instant", temperature=0)

prompt1=PromptTemplate(template="Give detailed report on {topic}.",
                       input_variables=["topic"])

prompt2=PromptTemplate(template="Generate 5 pointers from the following text: {text}",
                       input_variables=["text"])

parser=StrOutputParser()

chain= prompt1|llm|parser|prompt2|llm|parser

result=chain.invoke({'topic':'artificial intelligence'})
print(result)

chain.get_graph().print_ascii()