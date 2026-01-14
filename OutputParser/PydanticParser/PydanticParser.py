from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

llm=ChatGroq(model="llama-3.1-8b-instant", temperature=0.2)

class Person(BaseModel):
    name:str = Field(..., description="The person's full name")
    age:int =Field(..., description="The person's age in years")
    city:str= Field(..., description="The city where the person lives")
parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(template='Generate details.\n{format_instructions}',
                        input_variables=[],
                        partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain=template |llm |parser
result=chain.invoke({})
print(result)