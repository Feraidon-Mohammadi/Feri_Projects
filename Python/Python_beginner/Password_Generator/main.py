from tkinter import *
from tkinter import Tk, Label, Entry, Checkbutton, IntVar
import random
import string



def generate_password():
    # define functions of password
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    digi = string.digits
    special_carachter = string.punctuation
    
    
    all_charachter = upper_case + lower_case + digi + special_carachter
    password_lenght = 8
    
    password = "".join(random.choice(all_charachter) for i in range(password_lenght) )

    # Update the password Entry widget
    entry_pass.delete(0, END)
    entry_pass.insert(0, password)





# hide insert text and chang color on focus
def on_entry_focus(event):
    if entry_website.get() == "www.example.com":
        entry_website.delete(0, END)
        entry_website.config(fg='black')  # Change text color on focus
        
def on_entry_leave(event):
    if entry_website.get() == "":
        entry_website.insert(0, "www.example.com")
        entry_website.config(fg='gray')  # Change text color on leave




# hide insert text and chang color on focus
def on_entry_focus_email(event):
    if entry_email.get() == "example@email.com":
        entry_email.delete(0, END)
        entry_email.config(fg='black')  # Change text color on focus

def on_entry_leave_email(event):
    if entry_email.get() == "":
        entry_email.insert(0, "example@email.com")
        entry_email.config(fg='gray')  # Change text color on leave





def save_data():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_pass.get()
    with open("collected_data.txt", "r") as exist_data:
        exists = exist_data.read()



    log_file = "text.txt"
    with open("collected_data.txt" ,"a") as file:
        if not (website in exists and email in exists and password in exists):
            file.write(f" Website: {website} | Email: {email} | Password: {password}\n\n")
        elif website.strip() not in exists or email.strip() not in exists or password.strip() not in exists :
            print("Entry data can not be Empty")
            
        #with open("collected_data.txt", "w") as file:
            #data.write()
        

    entry_website.delete(0, END)
    entry_email.delete(0, END)
    entry_pass.delete(0, END)


def toggle_password_visibility():
    # Toggle the password visibility based on the checkbutton state
    if show_password_var.get():
        entry_pass.config(show="")
    else:
        entry_pass.config(show="*")


window = Tk()

window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=500)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(250, 100, image=logo_img)  # x and y positions need i did put 100 for both
canvas.grid(row=0, column=1)

frame = Frame()
frame.grid(row=1, column=0, columnspan=3)

website_label = Label(frame, text="Website")
website_label.grid(row=1)




placeholder_text = "www.example.com"
entry_website = Entry(frame, width=55, fg="gray", font=("Arial", 10))
entry_website.grid(row=1, column=1, columnspan=3)
entry_website.focus() # important when app started , cusor jump in to input
entry_website.insert(0, placeholder_text)




email_label = Label(frame, text="Email")
email_label.grid(row=2)

placeholder_text_email = "example@email.com"
entry_email = Entry(frame, width=55, fg="gray", font=("Arial", 10))
entry_email.grid(row=2, column=1, columnspan=3)
entry_email.insert(0, placeholder_text_email)





password_label = Label(frame, text="Password")
password_label.grid(row=3)

entry_pass = Entry(frame, width=30, show="*")
entry_pass.grid(row=3, column=1, columnspan=2, sticky="w")

show_password_var = IntVar()
show_password_check = Checkbutton(frame, variable=show_password_var, command=toggle_password_visibility,width=0)
show_password_check.grid(row=3, column=2, columnspan=1, pady=(1, 0), sticky="e")

generate_pass = Button(frame, text="Generate Password", width=20, command=generate_password)
generate_pass.grid(row=3, column=3, sticky="e")

button_add = Button(frame, text="Submit", width=35, command=save_data)
button_add.grid(row=4, column=1, columnspan=3)


# need for remove entry when focus on Entry
entry_website.bind("<FocusIn>", on_entry_focus)
entry_website.bind("<FocusOut>", on_entry_leave)



# need for remove entry when focus on Entry
entry_email.bind("<FocusIn>", on_entry_focus_email)
entry_email.bind("<FocusOut>", on_entry_leave_email)




window.mainloop()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
