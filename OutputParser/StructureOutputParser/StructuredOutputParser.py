#StructuredOutputParser removed from Langchain, so it doesnt work anymore.

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

# Initialize LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2
)

schema=[
    ResponseSchema(name='fact1', description='Fact1 about the topic'),
    ResponseSchema(name='fact2', description='Fact2 about the topic'),
    ResponseSchema(name='fact3', description='Fact3 about the topic')
]

parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(template='give 3 facts about the {topic} \n {format_instructions}',
                        input_variables=['topic'],
                        partial_variables={'format_instructions':parser.get_format_instructions()})

prompt=template.format(topic='moon')

result=llm.invoke(prompt)
output1=parser.parse(result.content)
print(output1)