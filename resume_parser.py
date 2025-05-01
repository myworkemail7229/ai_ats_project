import pdfplumber
from docx import Document

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return ' '.join(page.extract_text() for page in pdf.pages if page.extract_text())

def extract_text_from_docx(file):
    doc = Document(file)
    return ' '.join(p.text for p in doc.paragraphs)
