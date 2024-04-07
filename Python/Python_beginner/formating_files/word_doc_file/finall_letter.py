import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Create a new Word document
doc = docx.Document()

# Define the elements
absender_info = {
    "name": "Max Mustermann",
    "address": "Musterstraße 123",
    "plz": "12345 Erfurt",
}

empfenger_info = {
    "name": "Empfänger Name",
    "address": "Empfänger Adresse",
    "plz": "Empfänger PLZ",
}

datum = "21.12.2023"

betreff_text = "Ihr Betreff hier \n"

text_data = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ,Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris , nisi ut aliquip ex ea commodo consequat." ,
    "",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ,Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris , nisi ut aliquip ex ea commodo consequat.",
    "",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ,Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris , nisi ut aliquip ex ea commodo consequat.",
    "",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ,Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris , nisi ut aliquip ex ea commodo consequat.",
    "",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ,Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris , nisi ut aliquip ex ea commodo consequat.",
    ""
    "ich danke Ihnen im voraus,",
    ""]
gruß_info = "Ihr Name und Nachname"

# Add "absender info oben links" section
absender_section = doc.add_paragraph()
absender_section.add_run("Absender Info oben links").bold = True
absender_section.alignment = WD_ALIGN_PARAGRAPH.LEFT

absender_name = doc.add_paragraph()
absender_name.add_run(absender_info["name"])
absender_name.add_run("\n" + absender_info["address"])
absender_name.add_run("\n" + absender_info["plz"])

# Add "empfenger" section
empfenger_section = doc.add_paragraph()
empfenger_section.add_run("Empfänger").bold = True
empfenger_section.alignment = WD_ALIGN_PARAGRAPH.LEFT

empfenger_name = doc.add_paragraph()
empfenger_name.add_run(empfenger_info["name"])
empfenger_name.add_run("\n" + empfenger_info["address"])
empfenger_name.add_run("\n" + empfenger_info["plz"])

# Add "datum rechts" section
datum_section = doc.add_paragraph()
datum_section.add_run("Datum, " + datum)
datum_section.alignment = WD_ALIGN_PARAGRAPH.RIGHT

# Add "betreff" section with font size 16
betreff_section = doc.add_paragraph()
betreff_run = betreff_section.add_run(betreff_text)
betreff_run.font.size = Pt(14)
betreff_section.alignment = WD_ALIGN_PARAGRAPH.LEFT

# Add "sehr geehrte damen und heren" section
sehr_geehrte_section = doc.add_paragraph("Sehr geehrte Damen und Herren")





# Add text data with paragraphs and justify alignment (only once)
for paragraph_text in text_data:
    text_paragraph = doc.add_paragraph(paragraph_text)
    text_paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    text_paragraph.paragraph_format.space_before = Pt(0)
    text_paragraph.paragraph_format.space_after = Pt(0)
    #doc.add_paragraph("")    # add next line for every paragraph





# Add "Mit freundlichen Grüßen" section
gruß_section = doc.add_paragraph()
gruß_run = gruß_section.add_run("Mit freundlichen Grüßen:")
gruß_run.bold = True
gruß_section.add_run("\n" + gruß_info)

# Save the document to a file with a .docx extension
doc.save("your_document4.docx")