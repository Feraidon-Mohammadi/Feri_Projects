from PyPDF2 import PdfMerger
# pip install PyPDF2 if not worked than need upgrade
# pip install --upgrade PyPDF2
def merge_pdfs(input_pdfs, output_pdf):
    merger = PdfMerger()

    try:
        # Add each PDF to the merger
        for pdf_file in input_pdfs:
            merger.append(pdf_file)

        # Write the merged PDF to the output file
        with open(output_pdf, 'wb') as output_file:
            merger.write(output_file)

        print(f'Merged PDFs successfully. Output saved to {output_pdf}')

    except Exception as e:
        print(f'Error merging PDFs: {e}')

if __name__ == "__main__":
    # Specify the input PDF files and the output PDF file
    input_pdfs = ["input/pdf_one.pdf", "input/pdf_two.pdf"]  # Add more file names if needed
    output_pdf = "output/merged_output.pdf"

    # Merge the PDFs
    merge_pdfs(input_pdfs, output_pdf)