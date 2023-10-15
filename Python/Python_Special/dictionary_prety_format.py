########################################################################################################################
print(f"\n")
title = "print prety dictionary function".upper()
print(title.center(44, "="))
print(f"\n")


########################################################################################################################


# Custom function to format dictionaries for pretty printing
def format_dict(d, indent=0):
    result = ""
    for key, value in d.items():
        if isinstance(value, dict):
            result += " " * indent + f"{key}:\n"
            result += format_dict(value, indent + 4)
        else:
            result += " " * indent + f"{key}: {value}\n"
    return result

# Members
member1 = {
    "vor_name": "ali",
    "nach_name ": "akbari",
    "aga": "33",
    "birthday": "null",
    "address": {
        "country": "Detuschland",
        "city": "koeln",
        "street": "berg_str_32",
        "zipcod": "556434"
    }
}

# Call the custom function to format the member dictionary
formatted_member1 = format_dict(member1)

# Print the formatted dictionary
print(formatted_member1)

########################################################################################################################
print(f"\n")
title = " or use json ot print prety ".upper()
print(title.center(44, "="))
print(f"\n")
########################################################################################################################
for member, data in band.items():
    formatted_data = json.dumps(data, indent=4)
    print(f"Here is band info for {member}: {formatted_data}\n")