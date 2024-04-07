import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image

def process_pdf(pdf_path):
    # Your PDF processing code goes here
    print(f"Processing PDF: {pdf_path}")

def process_image(image_path):
    # Your image processing code goes here
    print(f"Processing image: {image_path}")

def on_drop(event):
    file_path = event.data.strip("{}")
    if file_path.lower().endswith('.pdf'):
        process_pdf(file_path)
    elif file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        process_image(file_path)
    else:
        print(f"Unsupported file type: {file_path}")

root = TkinterDnD.Tk()

# Configure the root window to accept dropped files
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)

root.geometry("300x200")
root.title("File Drop Example")

# You can add more GUI elements here

root.mainloop()