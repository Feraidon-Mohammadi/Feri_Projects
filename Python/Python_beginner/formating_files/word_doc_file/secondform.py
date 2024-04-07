from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

# Create a new Word document
doc = Document()

# Add a title
title = doc.add_heading('My Word Document', level=1)
title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

# Add a paragraph with long text
long_text = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ,Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris , nisi ut aliquip ex ea commodo consequat."
)

p = doc.add_paragraph(long_text)

# Set paragraph alignment
p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY

# Add another paragraph
p2 = doc.add_paragraph("Another paragraph with different formatting.")
p2.add_run(' Bold Text').bold = True
p2.add_run(' Italic Text').italic = True

# Change font size and style for the second paragraph
for run in p2.runs:
    run.font.size = Pt(12) if 'Bold' in run.text else Pt(10)

# Save the document
doc.save('sample.docx')