from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding=HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

document=[ "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query="Tell me something about rohit"

query_embedding=embedding.embed_query(query)
doc_embedding=embedding.embed_documents(document)

scores = cosine_similarity([query_embedding], doc_embedding)[0]

index = np.argmax(scores)
score = scores[index]

print(document[index], score)

