from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableBranch , RunnableLambda
from langchain_core.runnables import Runnable
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
load_dotenv()

#we use pydantic output parser to parse the sentiment analysis output and to get a static output , as the llm output may vary each time
model1 = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(...,description="give the sentiment of the feedback as positive or negative")

parser2=PydanticOutputParser(pydantic_object=Feedback)


prompt1=PromptTemplate(template="classify the sentiment of the following text into positive or negative \n {feedback} \n {format_instructions}.",
                       input_variables=["feedback"],
                       partial_variables={"format_instructions":parser2.get_format_instructions()})

classifier= prompt1| model1 | parser2

prompt2=PromptTemplate(template="Write a  reponse to positive feedback: {feedback}",
                       input_variables=['feedback'])

prompt3=PromptTemplate(template="Write a  response to negative feedback,apologize and offer solution: {feedback}",
                       input_variables=['feedback'])

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive',prompt2|model1|parser),
    (lambda x:x.sentiment=='negative',prompt3|model1|parser),
    RunnableLambda(lambda x: "No valid sentiment detected")
)

chain =classifier |branch_chain
result=chain.invoke({'feedback':"Wow what a nice product , really loved it!Superb quality and great value for money."})

print(result)   

chain.get_graph().print_ascii()