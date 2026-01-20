from langchain_community.document_loaders import PyPDFLoader


loaderr=PyPDFLoader('dl-curriculum.pdf')
docs=loaderr.load()
print(len(docs))  # Print number of pages loaded
print(docs[0].page_content)  #Print  content of the first page
print(docs[1].metadata)  #Print the metadata of second page


