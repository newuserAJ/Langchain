from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm=ChatGroq(model="llama-3.1-8b-instant", temperature=0)

prompt=PromptTemplate(template="Generate 5 facts about {topic}.",
                       input_variables=["topic"])

parser=StrOutputParser()

chain= prompt | llm | parser

result=chain.invoke({'topic':'cricket'}) 
print(result)

# graph of how the chain works the workflow
chain.get_graph().print_ascii()

