from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Initialize LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2
)

# Initialize JSON parser
parser = JsonOutputParser()

# Prompt template
template = PromptTemplate(
    template=(
        "Generate details of a person including name, age, and city.\n"
        "{format_instruction}"
    ),
    input_variables=[],
    partial_variables={
        "format_instruction": parser.get_format_instructions()
    }   #format_instruction tells the type of output we want from the model
)
'''
# Create prompt
prompt = template.format()

# Invoke model
response = llm.invoke(prompt)

# Parse output
parsed_output = parser.parse(response.content)
            OR  using chains
'''

chain =template | llm | parser
result=chain.invoke({})             #we have to pass a empty dict as there are no input variables
print(result)
