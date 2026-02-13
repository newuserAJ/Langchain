from langchain_text_splitters import CharacterTextSplitter

text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

splitter=CharacterTextSplitter(chunk_size=10,chunk_overlap=0,separator='')

result=splitter.split_text(text)
print(result)