import pdfplumber
from docx import Document


def load_pdf(path: str) -> str:
    text = ""
    pages =0;
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
                pages +=1;
    print("Total number of pages: ",pages) ## update 2
    return text


def load_docx(path: str) -> str:
    doc = Document(path)
    return "\n".join(para.text for para in doc.paragraphs)
