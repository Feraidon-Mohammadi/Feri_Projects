import os
from PyPDF2 import PdfReader, PdfWriter

def remove_pages(input_path, output_path, pages_to_remove):
    # Create output folder if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(input_path, 'rb') as input_file:
        pdf_reader = PdfReader(input_file)
        pdf_writer = PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            # Skip pages to be removed
            if page_num + 1 not in pages_to_remove:
                pdf_writer.add_page(pdf_reader.pages[page_num])

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

# Example usage for a single file
input_pdf_path = 'input_pdf/wohnung2.pdf'  # Specify the input PDF file
output_pdf_path = 'output_pdf/wohnung2.pdf'  # Specify the output PDF file
pages_to_remove = [5, 6, 7, 8, 9, 10, 11, 12, 13]  # Specify the page numbers to remove
# pages_to_remove = [1, 2, 3, 4, 5]

remove_pages(input_pdf_path, output_pdf_path, pages_to_remove)



