from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

code = '''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


def check_result(average):
    if average >= 40:
        return "Pass"
    return "Fail"
'''

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=200,
    chunk_overlap=20
)

chunks = splitter.split_text(code)

print(len(chunks))
print('\n---chuck 0----\n')
print(chunks[0])

# 3

# ---chuck 0----

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks