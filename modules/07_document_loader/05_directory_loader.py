from langchain_community.document_loaders import DirectoryLoader,TextLoader

loader=DirectoryLoader(
                        path='./modules/07_Document_loader/directory_samples',
                        glob='*.txt',
                        loader_cls=TextLoader)

doc=loader.load()
print(doc)  

#OUTPUT

# [Document(metadata={'source': 'modules\\07_Document_loader\\directory_samples\\dbms_notes.txt'}, page_content='Database Management Systems\n\nNormalization organizes relational tables to reduce redundancy and update anomalies.\n'), Document(metadata={'source': 'modules\\07_Document_loader\\directory_samples\\networks_notes.txt'}, page_content='Computer Networks\n\nTCP provides a reliable, ordered byte stream between applications.\n'), Document(metadata={'source': 'modules\\07_Document_loader\\directory_samples\\os_notes.txt'}, page_content='Operating Systems\n\nA process is a program in execution. A thread is a unit of execution within a process.\n')]