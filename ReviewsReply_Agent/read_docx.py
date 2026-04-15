from docx import Document
import os

filename = "April 2026.docx"
if os.path.exists(filename):
    doc = Document(filename)
    print("--- Contents of April 2026.docx ---")
    for para in doc.paragraphs:
        print(para.text)
    print("-----------------------------------")
else:
    print("File not found")
