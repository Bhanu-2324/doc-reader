from utils.loader import  load_pdf # , load_docx 
print("Test started");

pdf_text = load_pdf("data/uploads/sample.pdf")
print("PDF TEXT PREVIEW:")
print(pdf_text[:500])

# docx_text = load_docx("data/uploads/sample.docx")
# print("\nDOCX TEXT PREVIEW:")
# print(docx_text[:5000])