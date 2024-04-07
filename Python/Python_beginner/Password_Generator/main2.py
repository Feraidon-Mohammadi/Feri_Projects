import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame(root)
frame1.pack()  # Using pack manager for frame1

label1 = tk.Label(frame1, text="This is Label 1")
label1.grid(row=0, column=0)  # Trying to use grid manager for label1 inside a pack-managed frame





root.mainloop()