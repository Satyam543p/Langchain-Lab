from langchain_community.document_loaders import TextLoader

loader=TextLoader('./modules/07_Document_loader/sample_notes.txt',encoding='utf-8')

doc=loader.load()

print(doc)  
#Output:[Document(metadata={'source': './modules/07_Document_loader/sample_notes.txt'},
#                 page_content='LangChain Document Loader Practice\n\nTopic: Operating System Deadlocks\n\nA deadlock is a situation in which a group of processes are blocked because each process is waiting for a resource held by another process in the group.\n\nThe four necessary conditions for deadlock are:\n1. Mutual exclusion: at least one resource cannot be shared.\n2. Hold and wait: a process holds resources while waiting for additional resources.\n3. No preemption: resources cannot be forcibly taken away.\n4. Circular wait: a circular chain of processes exists, with each process waiting for a resource held by the next process.\n\nA system can prevent deadlock by ensuring that at least one necessary condition never holds.\n')]

#here document loaded in form of list of document objects( where metadata and page_contents are key)


print(type(doc))  ##  <class 'list'>
print(doc[0].page_content)  #Actual content of the page
print(doc[0].metadata)  # meta info of that page like page number,source etc.

