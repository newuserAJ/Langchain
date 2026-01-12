from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="allenai/Bolmo-1B",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
    max_new_tokens=256,
    temperature=0.7,
)

print(llm.invoke("What is the capital of India?"))