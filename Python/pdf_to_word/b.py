import fitz  # PyMuPDF
from docx import Document

def extract_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    word_doc = Document()

    for page_number in range(doc.page_count):
        page = doc[page_number]

        # Extract text
        text = page.get_text()
        word_doc.add_paragraph(text)

    doc.close()
    return word_doc

def save_word_document(word_doc, output_path):
    word_doc.save(output_path)

# Example usage
pdf_path = 'example.pdf'
output_path = 'output.docx'

# Extract text from PDF
word_document = extract_pdf_text(pdf_path)

# Save Word document
save_word_document(word_document, output_path)