line01 = "*****************************"
line02 = "*                           *"
line03 = "*         Welcome!          *"
line02 = "*                           *"
line04 = "*****************************"

print('')
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)

short_key = {" ctr + D  copy line ",
             "ctr + alt + L  == reformat document automatik"}
ganz_zahl = int(input("add your number: "))
bruch_zahl = int(input("add your division number "))
liste = []
rund = round(ganz_zahl / bruch_zahl)
liste = [rund]
print(liste)

##############################################################################
"""
import os
# Function to clear the console
def clear_console():
    if os.name == 'posix':  # Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':   # Windows
        os.system('cls')
clear_console()
print("This is a cleared console.")
"""


