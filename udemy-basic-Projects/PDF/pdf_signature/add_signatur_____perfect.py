import fitz  # PyMuPDF

def add_signature(input_pdf, signature_image, output_pdf, stamp_size=(3, 3)):
    pdf_document = fitz.open(input_pdf)

    # Iterate through each page in the input PDF
    for page_num in range(len(pdf_document)):
        pdf_page = pdf_document[page_num]

        # Get the dimensions of the PDF page
        page_rect = pdf_page.rect

        # Open the signature image
        img = fitz.Pixmap(signature_image)
    
        
        # Calculate the new size for the signature stamp
        stamp_width = page_rect.width * stamp_size[0] / 6 + 90
        stamp_height = page_rect.height * stamp_size[1] / 6 + 100

        # Calculate the position for the bottom right corner of the stamp
        

        # Overlay the signature image onto the PDF page
        pdf_page.insert_image((400, 300,page_rect.x1 - stamp_width + 290,page_rect.y1 + 100 - stamp_height +750 ), pixmap=img)

        # Free the Pixmap resources
        img = None

    # Save the modified PDF to the output file
    pdf_document.save(output_pdf)
    pdf_document.close()

# Example usage
input_pdf = 'pdf_need_signature/pdf_one1.pdf'
signature_image = 'signature_img/EK2.png'
output_pdf = 'output/output.pdf'
add_signature(input_pdf, signature_image, output_pdf)