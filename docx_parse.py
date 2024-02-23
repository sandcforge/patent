import docx

def parse_element(element):
    # Extract text and formatting (e.g., bold, italic, font size)
    text = ""
    for run in element.runs:
        text += run.text
    print(text)




filename = "files/en3.docx"
en_file = docx.Document(filename)

for element in en_file.paragraphs:
    parse_element(element)
    print("=======================")