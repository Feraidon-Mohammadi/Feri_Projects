import fitz  # PyMuPDF
import docx


def pdf_to_docx(pdf_path, docx_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    #path= "C:\\Users\\admin\\PycharmProjects\\Py_beginner\\pdf_to_word"

    # Create a Word document
    doc = docx.Document()

    # Iterate through each page of the PDF
    for page_number in range(pdf_document.page_count):
        # Get the text from the PDF page
        pdf_page = pdf_document.load_page(page_number)
        pdf_text = pdf_page.get_text()

        # Add the text to the Word document
        doc.add_paragraph(pdf_text)

    # Save the Word document
    doc.save(docx_path)

    # Close the PDF document
    pdf_document.close()


# Example usage
pdf_to_docx('example.pdf', 'output.docx')