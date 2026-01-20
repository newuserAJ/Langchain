'''The time to compute increases with the number of documents and pages in the directory and is loadedd on to the memory. 
Therefore we require better options of the purpose of loading documents from a directory.

For better load time we can use lazy_loading which loads the documents one at a time when required instead of 
loading all at once into the memory.
'''

from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

#specified the path, type of document to extract and the type of loader class to use which is PyPDFLoader in this case
loaderr=DirectoryLoader(path='BOOKS',glob='*.pdf',loader_cls=PyPDFLoader)  

docs=loaderr.lazy_load()

# print(len(docs))  #Print the number of documents aka the no. of total pages loaded from all pdfs in the directory

#Print the content of the first page of the first document 
# print(docs.page_content)

# #Print the metadata of the first page of the first document which includes name,type etc.
# print(docs[0].metadata)

#Using lazy loading to load documents one at a time
'''lazy_loader=DirectoryLoader(path='BOOKS',glob='*.pdf',loader_cls=PyPDFLoader,lazy_load=True)'''

for doc in docs:
    print(doc.metadata)   #Faster output to load docs one at a time  