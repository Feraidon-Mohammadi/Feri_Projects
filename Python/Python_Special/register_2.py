anrede = input("Anrede Auswählen Herr/Frau/Divers: ")
is_herr = anrede == "Herr"
is_frau = anrede == "Frau"
is_divers = anrede == "Divers"

users_info_list = []

if is_herr or is_frau or is_divers:
    print(f"Welcome {anrede}")

    # Create a dictionary to store user information
    user_info_dictionary = {}

    def validation(value_str):
        while True:
            if not any(char.isdigit() for char in value_str):
                return value_str
            else:
                print("Invalid input! Bitte geben Sie eine korrekte Eingabe ein: ")
                value_str = input("Wert eingeben: ")

    # Collect user information based on the chosen salutation
    user_info_dictionary["Anrede"] = anrede
    user_info_dictionary["Benutzer_Name"] = validation(input("BenutzerName: "))
    user_info_dictionary["Name"] = validation(input("Name: "))
    user_info_dictionary["Nach_Name"] = validation(input("Nach Name: "))

    # Append the user_info_dictionary to the users_info_list
    users_info_list.append(user_info_dictionary)

    # Print the collected user information
    print("User Information:")
    print(users_info_list)
else:
    print("Invalid salutation. Please choose Herr, Frau, or Divers.")