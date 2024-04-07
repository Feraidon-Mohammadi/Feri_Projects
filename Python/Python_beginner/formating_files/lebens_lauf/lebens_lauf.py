import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

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
#header.add_picture('kk.jpeg', width=docx.shared.Inches(1.5), height=docx.shared.Inches(1))

# Add your personal information on the right side
personal_info = doc.add_paragraph()
personal_info.add_run("Kommunikation\nProjektmanagement\nIT-Recht\nMarketing\nBerufsbezogene Mathematik\nRechnerarchitektur\nNetzwerk\nWindows 10\nManaging Modern Desktops\nWindows Server Netzwerk, Administration und Identitätsverwaltung\nWindows Server Projekt\nMicrosoft DevOps\nSecurity+\nSoftware Engineering und Programmierlogik\nprozedurale Programmierung\nDatenbanktheorie\nProgrammieren einer Microsoft SQL Server Datenbank\nAdministration einer SQL Datenbank\nProgrammierung mit C# und .NET")

# Format the right-side information
right_side = personal_info.runs[0]
right_side.bold = True
right_side.font.size = Pt(16)
right_side.alignment = WD_ALIGN_PARAGRAPH.RIGHT

# Add your skills and languages on the left side
left_info = doc.add_paragraph()
left_info.add_run("KENNTNISSE\nPROGRAMMIERUNGSPRACHEN UND IT\nPython, Java, C#, SQL, PHP, JavaScript, FrontEnd, HTML, CSS\nICDL, CompTIA (Network-plus, security-plus), Grundkenntnisse Certified Ethical hacking\nLinux Grundkenntnisse, MS Azure, MD100, Windows Server 2022, MD101\n\nSPRACHKENNTNISSE\nPersisch - Muttersprache\nEnglisch - B2\nDeutsch - B2")

# Format the left-side information
left_side = left_info.runs[0]
left_side.bold = True
left_side.font.size = Pt(16)
left_side.alignment = WD_ALIGN_PARAGRAPH.LEFT

# Add your work experience
work_experience = doc.add_paragraph("logistig Meidengroup, Erfurt (font 16 hier)\nFunke Mediengruppe, Erfurt\nMai 2019 - Dezember 2021")

# Format the work experience
work_experience.runs[0].bold = True
work_experience.runs[0].font.size = Pt(16)

# Add education information
education_info = doc.add_paragraph("BILDUNGSINFORMATIONEN HIER (font 16)\nSome info here")

# Format the education information
education_info.runs[0].bold = True
education_info.runs[0].font.size = Pt(16)

# Add contact information
contact_info = doc.add_paragraph("CONTACT INFORMATION (font 16)\nHere some info")

# Format the contact information
contact_info.runs[0].bold = True
contact_info.runs[0].font.size = Pt(16)

# Save the document to a file with a .docx extension
doc.save("your_cv.docx")