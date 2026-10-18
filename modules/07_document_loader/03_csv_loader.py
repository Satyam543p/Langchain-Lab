from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path='./modules/07_Document_loader/sample_students.csv')

doc=loader.load() #here each we document object for each and information of each row is in one document object

print(doc)

# [Document(metadata={'source': './modules/07_Document_loader/sample_students.csv', 'row': 0}, page_content='student_id: S101\nname: Aarav\nsubject: Operating Systems\nscore: 84'), Document(metadata={'source': './modules/07_Document_loader/sample_students.csv', 'row': 1}, page_content='student_id: S102\nname: Diya\nsubject: Computer Networks\nscore: 91'), Document(metadata={'source': './modules/07_Document_loader/sample_students.csv', 'row': 2}, page_content='student_id: S103\nname: Kabir\nsubject: DBMS\nscore: 78'), Document(metadata={'source': './modules/07_Document_loader/sample_students.csv', 'row': 3}, page_content='student_id: S104\nname: Meera\nsubject: Algorithms\nscore: 88')]

