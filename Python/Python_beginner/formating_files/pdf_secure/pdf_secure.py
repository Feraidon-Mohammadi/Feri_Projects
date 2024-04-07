from PyPDF2 import PdfReader, PdfWriter
import argparse

def protect_pdf(filename, password):
	pdf_reader = PdfReader(filename)
	pdf_writer = PdfWriter()
	
	for page in range(len(pdf_reader.pages)):
		pdf_writer.add_page(pdf_reader.pages[page])
		
	pdf_writer.encrypt(user_password=password, use_128bit=True)
	
	output_filename = filename + ".protected.pdf"
	with open(output_filename, "wb") as out:
		pdf_writer.write(out)
		
	print(f"{filename} has been protected")
	
	

def main():
	parser = argparse.ArgumentParser(description="Protect a PDF File. ")
	parser.add_argument('-n', '--name', required=True)
	parser.add_argument('-p', '--password', required=True)
	args = parser.parse_args()
	
	protect_pdf(args.name, args.password)

# python pdf_secure.py -n "English.pdf" -p "PasswordPassword"
# python pdf_secure.py -n "English.pdf" -p "Password$"

if __name__=="__main__":
	main()
	#worked
	