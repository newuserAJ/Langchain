from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.runnables import Runnable
load_dotenv()

model1 = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
model2 = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

prompt = PromptTemplate(
    template="Generate notes on the topic: {topic}.",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="From the followning notes, generate a set of questions and answers for a quiz : {notes}",
    input_variables=["notes"]
)

prompt3 = PromptTemplate(
    template="Merge the notes and the quiz into a single dodument from notes: {notes}  and quiz: {quiz}",
    input_variables=["notes", "quiz"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": prompt | model1 | parser
})

quiz_chain = prompt2 | model2 | parser
merge_chain = prompt3 | model1 | parser

chain = (
    parallel_chain
    | RunnablePassthrough.assign(
        quiz=lambda x: quiz_chain.invoke({"notes": x["notes"]})
    )
    | merge_chain
)
text = "The solar system is made up of the Sun and all the objects that orbit it, including planets, moons, asteroids, comets, and meteoroids. The eight planets in our solar system are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. Each planet has its own unique characteristics, such as size, composition, atmosphere, and distance from the Sun. The solar system also contains dwarf planets like Pluto, as well as countless smaller objects that contribute to its complexity and diversity."
result = chain.invoke({"topic": text})
print(result)

chain.get_graph().print_ascii()
