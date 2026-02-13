from langchain_text_splitters import CharacterTextSplitter

text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

splitter=CharacterTextSplitter(chunk_size=10,chunk_overlap=0,separator='')

result=splitter.split_text(text)
print(result)

#for using text splitter with documents, you can use the following code:
# from langchain.document_loaders import PyPDFLoader

# loader=PyPDFLoader('example.pdf')
# doc=loader.load()
# splitter=CharacterTextSplitter(chunk_size=10,chunk_overlap=0,separator='')
# results=splitter.split_documents(doc)