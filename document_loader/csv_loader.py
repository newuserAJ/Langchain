from langchain_community.document_loaders import CSVLoader

#each row of the csv file is treated as a document
loader=CSVLoader(file_path='Social_Network_Ads.csv', encoding='utf-8') 
docs=loader.load()
print(docs[0])  #Prints the first row of the csv file 
print(docs)