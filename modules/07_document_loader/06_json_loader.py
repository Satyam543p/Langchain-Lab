from langchain_community.document_loaders import JSONLoader

loader=JSONLoader(file_path='./modules/07_Document_loader/sample_records.json' ,
                  jq_schema=".records[]",
                  text_content=False )

doc=loader.load()

print(doc)
