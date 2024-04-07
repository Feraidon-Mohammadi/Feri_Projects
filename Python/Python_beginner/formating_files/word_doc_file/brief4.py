import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Create a new Word document
doc = docx.Document()

# Define the elements
absender_info = {
    "name": "Max Mustermann",
    "address": "Musterstraße 123",
    "plz": "12345",
}

empfenger_info = {
    "name": "Empfänger Name",
    "address": "Empfänger Adresse",
    "plz": "Empfänger PLZ",
}

datum = "21.12.2023"

betreff_text = "Ihr Betreff hier"

text_data = [
            "Hiermit bewerbe ich mich bei Ihnen um eine Praktikum Stelle im Bereich IT-Sicherheit, welches ich am 25.09.2023 beginnen möchte.",
        "Durch Ihre Webseite habe ich mich über Ihre Firma informiert.",
        "Falls es bei Ihnen die Möglichkeit für Praktikumsstellen im Bereich Sicherheit gibt, möchte ich meine Chance mit dieser Bewerbung bei Ihrem Unternehmen prüfen.",
        "Mein langfristiges Ziel liegt jedoch im Bereich IT-Sicherheit, insbesondere im Bereich Penetrationstests und -prüfung.",
        "Während meiner Umschulung bei IAD habe ich bereits erste Erfahrungen in der Sicherheit und Anwendungsentwicklung gesammelt und grundlegende Kenntnisse in Sicherheit erworben: Security Plus CompTIA und Network Plus CompTIA, Ethical Hacking und verschiedenen Programmiersprachen wie Python, SQL, C#, Java. Weitere Informationen stehen in meinem Lebenslauf zur Verfügung.",
     
]

gruß_info = "Ihr Name und Nachname"

# Add text data with paragraphs and justify alignment
for paragraph_text in text_data:
    text_paragraph = doc.add_paragraph(paragraph_text)
    text_paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY





# Add "absender info oben links" section
absender_section = doc.add_paragraph()
absender_section.add_run("Absender Info oben links").bold = True
absender_section.alignment = WD_ALIGN_PARAGRAPH.LEFT

absender_name = doc.add_paragraph()
absender_name.add_run(absender_info["name"])
absender_name.add_run(", " + absender_info["address"])
absender_name.add_run("\n" + absender_info["plz"])

# Add "empfenger" section
empfenger_section = doc.add_paragraph()
empfenger_section.add_run("Empfänger").bold = True
empfenger_section.alignment = WD_ALIGN_PARAGRAPH.LEFT

empfenger_name = doc.add_paragraph()
empfenger_name.add_run(empfenger_info["name"])
empfenger_name.add_run(", " + empfenger_info["address"])
empfenger_name.add_run("\n" + empfenger_info["plz"])

# Add "datum rechts" section
datum_section = doc.add_paragraph()
datum_section.add_run("Datum, " + datum)
datum_section.alignment = WD_ALIGN_PARAGRAPH.RIGHT

# Add "betreff" section with font size 16
betreff_section = doc.add_paragraph()
betreff_run = betreff_section.add_run(betreff_text)
betreff_run.font.size = Pt(16)
betreff_section.alignment = WD_ALIGN_PARAGRAPH.LEFT

# Add "sehr geehrte damen und heren" section
sehr_geehrte_section = doc.add_paragraph("Sehr geehrte Damen und Herren")

# Add text data with paragraphs
for paragraph_text in text_data:
    text_paragraph = doc.add_paragraph(paragraph_text)

# Add "Mit freundlichen Grüßen" section
gruß_section = doc.add_paragraph()
gruß_run = gruß_section.add_run("Mit freundlichen Grüßen:")
gruß_run.bold = True
gruß_section.add_run("\n" + gruß_info)

# Save the document to a file with a .docx extension
doc.save("your_document.docx")