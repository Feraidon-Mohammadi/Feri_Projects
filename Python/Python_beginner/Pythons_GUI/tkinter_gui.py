import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

root = tk.Tk()
root.title("Tkinter GUI")



w = root.width = 500
h = root.hight = 300
root.geometry(f"{w}x{h}")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Click me!", command=on_button_click)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()

"""
##############################################################################################################
########################## to show the window just thats enough ##############################################
##############################################################################################################



import tkinter as tk


root = tk.Tk()
root.title("Tkinter GUI")



root.mainloop()


"""