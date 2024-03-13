import tkinter as tk
from tkinter import Label


def wufeln():
    pass

def main():

    root = tk.Tk()
    window = root.title("feri game")



    w = root.width = 500
    h = root.hight = 300
    root.geometry(f"{w}x{h}")


    wurfel_size_x = w / 2 + 2
    wurfel_size_y = h / 2 + 2

    head = wurfel_size_x + wurfel_size_y



    label = Label()
    label.grid(row=2, column=1)

    label1 = Label()


    wurfel = w / 2 + h /2




    root.mainloop()


if __name__ == "__main__":
    main()

























