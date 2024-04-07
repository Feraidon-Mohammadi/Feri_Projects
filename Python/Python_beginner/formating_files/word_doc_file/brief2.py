from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Create a new Word document
doc = Document()

# Add "absender info oben links" section
absender_info = doc.add_paragraph()
absender_info.add_run("Name, Vorname")
absender_info.add_run("\nAddress, PLZ")

# Add "empfenger" section
empfenger = doc.add_paragraph()
empfenger.add_run("Name, Vorname")
empfenger.add_run("\nAddress, PLZ")

# Add "datum rechts" section
datum = doc.add_paragraph()
datum.add_run("Den, 21.12.2023")
datum.alignment = WD_ALIGN_PARAGRAPH.RIGHT

# Add "betreff" section with font size 16
betreff = doc.add_paragraph()
betreff.add_run("Betreff").bold = True
betreff.runs[0].font.size = Pt(16)

# Add "sehr geehrte damen und heren" section
sehr_geehrte = doc.add_paragraph("Sehr geehrte Damen und Herren")

# Add text data with paragraphs
text_data = [
    "Alle Textdaten here mit Paragraphen",
    "Text beendet?",
]

for paragraph_text in text_data:
    paragraph = doc.add_paragraph(paragraph_text)

# Add "Mit freundlichen Grüßen" section
gruß = doc.add_paragraph()
gruß.add_run("Mit freundlichen Grüßen:")
gruß.add_run("\nName and Nachname")

# Save the document to a file
doc.save("your_document.doc")

# Replace "your_document.doc" with the desired file name.