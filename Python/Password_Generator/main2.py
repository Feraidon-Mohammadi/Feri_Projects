import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame(root)
frame1.pack()  # Using pack manager for frame1

label1 = tk.Label(frame1, text="This is Label 1")
label1.grid(row=0, column=0)  # Trying to use grid manager for label1 inside a pack-managed frame





root.mainloop()


"""




    while True:
        with open("collected_data.txt", "a+") as file:
            exists = file.read()
            if not (website in exists and email in exists):
                file.write(f" Website: {website} | Email: {email} | Password: {password}\n\n")
                messagebox.showinfo("Correct Input", "generated Password successfull!")
                break

            elif website.strip() in exists and email.strip() in exists:
                messagebox.showerror(title="Exist data", message="The data you entered already exist")
                break

            elif not password or not website or not email :
                messagebox.showerror(title="Exist data", message="The data you entered already exist")
                break
            file.seek(0)  # Reset file pointer to the beginning


























"""