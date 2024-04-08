# import fitz  # PyMuPDF
# from docx import Document
#
# def pdf_to_docx(pdf_path, docx_path):
#     doc = Document()
#
#     # Open the PDF file
#     pdf_document = fitz.open(pdf_path)
#
#     for page_num in range(pdf_document.page_count):
#         # Extract text from each page
#         page = pdf_document[page_num]
#         text = page.get_text()
#
#         # Add the extracted text to the Word document
#         doc.add_paragraph(text)
#
#     # Save the Word document
#     doc.save(docx_path)
#
#     print(f"Conversion successful. DOCX file saved at: {docx_path}")
#
# if __name__ == "__main__":
#     # Specify the path to your PDF file and the desired output DOCX file
#     pdf_file_path = "path/to/your/file.pdf"
#     docx_output_path = "path/to/your/output/file.docx"
#
#     pdf_to_docx(pdf_file_path, docx_output_path)
import os

from pdf2docx import Converter

def pdf_to_docx(input_folder, output_folder):
    # Check if the input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return

    # Check if the output folder exists; if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for pdf_file in os.listdir(input_folder):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, pdf_file)
            docx_file = os.path.splitext(pdf_file)[0] + "_output.docx"
            docx_path = os.path.join(output_folder, docx_file)

            convert_pdf_to_docx(pdf_path, docx_path)

def convert_pdf_to_docx(pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()

    print(f"Conversion successful. DOCX file saved at: {docx_path}")

if __name__ == "__main__":
    # Specify the input and output folders (using relative paths)
    input_folder = "input_folder"
    output_folder = "output_folder"

    pdf_to_docx(input_folder, output_folder)