from utils.loader import   load_pdf # ,  load_docx
from utils.chunker import chunk_text

pdf_text = load_pdf("data/uploads/sample.pdf")
chunks = chunk_text(pdf_text)

# docx_text = load_docx("data/uploads/sample.docx")
# chunks = chunk_text(docx_text)

print("Total chunks:", len(chunks))
print("First chunk preview:\n", chunks[0][:3000])
