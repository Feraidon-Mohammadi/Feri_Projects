import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches
from docx.oxml.ns import qn  # Import 'qn' from 'docx.oxml' module
from docx.oxml import OxmlElement  # Import 'OxmlElement' from 'docx.oxml' module

# Create a new Word document
doc = docx.Document()

# Set Page Background Color
section = doc.sections[0]
bg_color = section.footer.paragraphs[0].add_run()
shading_el = OxmlElement('w:shd')
shading_el.set(qn('w:fill'), '0066cc')
bg_color._r.insert(0, shading_el)

# Set Header with a Picture
header = doc.sections[0].header
header_paragraph = header.paragraphs[0]

# Add a picture to the header as a shape
picture = header_paragraph.add_run().add_picture('kk.jpeg', width=Inches(1.5), height=Inches(1))

# Position the picture in the header
picture.alignment = WD_ALIGN_PARAGRAPH.LEFT

# Add your personal information on the right side
personal_info = doc.add_paragraph()
personal_info.add_run("Kommunikation\nProjektmanagement\nIT-Recht\nMarketing\nBerufsbezogene Mathematik\nRechnerarchitektur\nNetzwerk\nWindows 10\nManaging Modern Desktops\nWindows Server Netzwerk, Administration und Identitätsverwaltung\nWindows Server Projekt\nMicrosoft DevOps\nSecurity+\nSoftware Engineering und Programmierlogik\nprozedurale Programmierung\nDatenbanktheorie\nProgrammieren einer Microsoft SQL Server Datenbank\nAdministration einer SQL Datenbank\nProgrammierung mit C# und .NET")

# Format the right-side information
right_side = personal_info.runs[0]
right_side.bold = True
right_side.font.size = Pt(16)
right_side.alignment = WD_ALIGN_PARAGRAPH.RIGHT

# ... (continue with the rest of your CV content)

# Save the document to a file with a .docx extension
doc.save("your_cv.docx")