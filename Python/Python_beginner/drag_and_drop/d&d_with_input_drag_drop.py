import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image
from PyPDF2 import PdfReader



def process_pdf(pdf_path):
    # Your PDF processing code goes here
    print(f"Processing PDF: {pdf_path}")
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        # Process PDF content as needed
        # Example: Print the number of pages
        num_pages = len(pdf_reader.pages)
        print(f"Number of pages: {num_pages}")
        
        
        
def process_image(image_path):
    # Your image processing code goes here
    print(f"Processing image: {image_path}")
    image = Image.open(image_path)
    # Process image as needed

def on_drop_pdf(event):
    pdf_file_path = event.data.strip("{}")
    if pdf_file_path.lower().endswith('.pdf'):
        process_pdf(pdf_file_path)
    else:
        print(f"Unsupported file type for PDF: {pdf_file_path}")

def on_drop_image(event):
    image_file_path = event.data.strip("{}")
    if image_file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        process_image(image_file_path)
    else:
        print(f"Unsupported file type for image: {image_file_path}")

root = TkinterDnD.Tk()

# Configure the root window to accept dropped files for PDF
pdf_frame = tk.Frame(root, width=150, height=150, borderwidth=2, relief="solid")
pdf_frame.pack(side=tk.LEFT, padx=10)
pdf_frame.drop_target_register(DND_FILES)
pdf_frame.dnd_bind('<<Drop>>', on_drop_pdf)
pdf_label_pdf = tk.Label(pdf_frame, text="Drop PDF here", font=("Helvetica", 10))
pdf_label_pdf.pack(expand=True)

# Configure the root window to accept dropped files for image
image_frame = tk.Frame(root, width=150, height=150, borderwidth=2, relief="solid")
image_frame.pack(side=tk.RIGHT, padx=10)
image_frame.drop_target_register(DND_FILES)
image_frame.dnd_bind('<<Drop>>', on_drop_image)
pdf_label_image = tk.Label(image_frame, text="Drop image here", font=("Helvetica", 10))
pdf_label_image.pack(expand=True)

root.geometry("400x200")
root.title("File Drop Example")

root.mainloop()