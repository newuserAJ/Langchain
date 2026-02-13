from langchain_text_splitters import RecursiveCharacterTextSplitter

text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0
)

result=splitter.split_text(text)
print(len(result))
print(result)
