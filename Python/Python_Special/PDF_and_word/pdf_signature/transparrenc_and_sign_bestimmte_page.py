import fitz  # PyMuPDF

def add_signature(input_pdf, signature_image, output_pdf, stamp_size=(3, 3), pages_to_sign=None):
    if pages_to_sign is None:
        pages_to_sign = []  # If pages_to_sign is not provided, sign all pages
    
    pdf_document = fitz.open(input_pdf)
    
    # Iterate through each page in the input PDF
    for page_num in range(len(pdf_document)):
        pdf_page = pdf_document[page_num]
        
        # Check if the current page is in the list of pages to sign
        if page_num + 1 in pages_to_sign:
            # Get the dimensions of the PDF page
            page_rect = pdf_page.rect
            
            # Open the signature image
            img = fitz.Pixmap(signature_image)
            
            # Calculate the new size for the signature stamp
            # stamp_width = page_rect.width * stamp_size[0] / 6 + 90  ## standard size
            signatur_size = 200 # change sige of signature
            stamp_width = page_rect.width * stamp_size[0] / 6 + signatur_size
            signatur_up_down = 460 # signature location up or down
            stamp_height = page_rect.height * stamp_size[1] / 6 + signatur_up_down
            
            # Calculate the position for the bottom right corner of the stamp
            # Overlay the signature image onto the PDF page  # plus overly and alpha for transparrency
            move_left = 280  # move it to left
            pdf_page.insert_image((move_left, 250, page_rect.x1 - stamp_width + 290, page_rect.y1 + 100 - stamp_height + 620),
                                  pixmap=img, overlay=False, alpha=0.8)
            
            # Free the Pixmap resources
            img = None
    
    # Save the modified PDF to the output file
    pdf_document.save(output_pdf)
    pdf_document.close()

# Example usage: Sign only the first and third pages
input_pdf = 'pdf_need_signature/test.pdf'
signature_image = 'signature_img/sing4.jpg'
output_pdf = 'output/output.pdf'
# pages_to_sign = [1, 3]
pages_to_sign = [1]
add_signature(input_pdf, signature_image, output_pdf, pages_to_sign=pages_to_sign)