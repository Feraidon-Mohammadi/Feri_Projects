from pdf2docx import Converter


def pdf_to_docx(pdf_path, docx_path):
    # Convert PDF to Word document
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()

# Example usage
pdf_to_docx('example.pdf', 'output.docx')