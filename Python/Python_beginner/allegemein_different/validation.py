


line1 =      "******************************************"
line3 =      "*           input validateion            *"
line5 =      "******************************************"
#print(line1)
#print(line3)
#print(line5)
space = f"\n"
########################################################################################################################
"""
def validation_str(input_text):
    while True:
        if not any(char.isdigit() for char in input_text):

            return input_text
        else:
         print("invalid input!. please try again: ")
        break

"""
#######################################################################################################################

title = "reverse funktion".upper()
print(title.center(44, "="))
print()
#######################################################################################################################

zahl_liste= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
revers_liste = []

def reversation():
    for i in range(len(zahl_liste) -1, -1, -1):
        # -1 -1 -1 # first-1(start from last element of list oder von )
        # second-1(end rang bis ende des list or alle bis ende )
        # third-1(pick next number with distans 1  )
        revers_liste.append(zahl_liste[i])


reversation()
reversed_list = revers_liste
print(reversed_list)




##############################################################################################
anrede = input("Anrede Auswählen Herr/Frau/Divers: ")
is_herr = anrede == "herr"
is_frau= anrede == "frau"
is_divers = anrede == "divers"





users_info_list = []


if is_herr :
    print("Welcome Herr")
    users_info_list.append("Herr")
    current_person = []
    user_info_dictionary =[]


    def validation(value_str):

        while True:
            current_person.append(value_str)
            if not any(char.isdigit() for char in value_str):

                return value_str
                benutzer_Name = {"Benutzer_Name": validation(input("BenutzerName: "))}
                current_person.append(value_str)
                print(current_person)
            else:
                print("Invalid input!. Bitte eingabe richtig eingeben: ")
                current_person.clear()
                break

            current_person.append(value_str)
            if not any(char.isdigit() for char in value_str):
                return value_str
                name = {"Name": validation(input("Name: "))}
                current_person.append(value_str)
                print(current_person)
            else:
                print("Invalid input!. Bitte eingabe richtig eingeben: ")
                current_person.clear()
                break


            if not any(char.isdigit() for char in value_str):
                return value_str
                nach_name = {"nach_name": validation(input("Nach Name: "))}
                current_person.append(value_str)
                print(current_person)
            else:
                print("Invalid input!. Bitte eingabe richtig eingeben: ")
                current_person.clear()
                break


        #current_person.clear() #-liste leeren
        print(current_person) #-rufe die liste



    benutzer_Name = {"Benutzer_Name": validation(input("BenutzerName: "))},
    name = {"Name": validation(input("Name: "))}
    nach_name = {"nach_name": validation(input("Nach Name: "))}
"""

    user_info_dictionary = {"Benutzer_Name": validation(input("BenutzerName: ")),
                            "Name": validation(input("Name: ")),
                            "nach_name": validation(input("Nach Name: "))}




    #add to list
    users_info_list.append(f"{user_info_dictionary} Address: ")
    user_address_Dictionary = {"country": str(input("Country: ")),
                               "City": str(input("City: ")),
                               "Street": str(input("Street: ")),
                               "zipcode": int(input("Zipcod: "))}
    #add to list
    users_info_list.append(user_address_Dictionary)


"""



"""

if is_frau :
    current_person = []
    current_person_address= []
    print("greeting for Frau")
    users_info_list.append("Frau")
    user_info_dictionary = {f"{validation(prompt=username)}":"",
    #user_info_dictionary = {"Benutzer_Name": str(input("Benutzer Name: ",f"{validation()}")),
                            "Name": str(input("Name: ")),
                            "Nach_Name": str(input("Nach Name: "))}
    current_person.append(user_info_dictionary)

    if user_info_dictionary[Benutzer_Name]== False:
        #current_person.clear(current_person[Benutzer_Name])
        benutzer_name = {"Benutzer_Name":str(input("bitte noch mall Benutzer Name eingeben: "))}
        current_person.append[benutzer_name]

    elif user_info_dictionary[Name] == False:
        #current_Herr.clear(current_person["Name"])
        name = {"Name": str(input("bitte noch mach Ihre Name richtig eingeben: "))}
        current_person.append[name]

    elif user_info_dictionary[Nach_Name] == False:
        #current_person.clear(current_person[Nach_Name])
        nach_Name = {"Nach_Name": str(input("Nach Name bitte richtig eingben: "))}
        current_person.append[nach_Name]

    user_info_dictionary.append(current_person)# add to list
    users_info_list.append(user_info_dictionary)
    Print(users_info_list)

    #############################################

    user_address_Dictionary = {"country": str(input("Country: ")),
                               "City": str(input("City: ")),
                               "Street": str(input("Street: ")),
                               "zipcode": int(input("Zipcod: "))}
    current_person_address.append(user_address_Dictionary)# add to list current

    if user_address_Dictionary(1) == False:
        current_person.clear(current_person(1))
        country = {"country": str(input("bitte noch mall Country Name eingeben: "))}
        current_person.append(country)

    elif user_address_Dictionary(2) == False:
        current_Herr.clear(current_person(2))
        city = {"city": str(input("bitte noch mal Ihre City Name richtig eingeben: "))}
        current_person.append(city)

    elif user_address_Dictionary(3) == False:
        current_person.clear(current_person(3))
        street = {"street": str(input("Street Name bitte richtig eingben: "))}
        current_person.append(street)

    elif user_address_Dictionary(4) == False:
        current_person.clear(current_person(4))
        zipcond = {"zipcond": str(input("zipcond bitte richtig eingben: "))}
        current_person.append(zipcond)
print(users_info_list)











if is_divers:
    print("Greeting for Divers")
    users_info_list.append("Divers")
    user_info_dictionary = {"Benutzer_Name": str(input("Benutzer Name: ")),
                            "Name": str(input("Name: ")),
                            "nach_name": str(input("Nach Name: "))}
    # add to list
    users_info_list.append(user_info_dictionary)
    user_address_Dictionary = {"country": str(input("Country: ")),
                               "City": str(input("City: ")),
                               "Street": str(input("Street: ")),
                               "zipcode": int(input("Zipcod: "))}
    # add to list
    users_info_list.append(user_address_Dictionary)

"""
print(users_info_list)




#= [f"Anrede: {e},User Address: {address}, User Information: {user_info} "]


















