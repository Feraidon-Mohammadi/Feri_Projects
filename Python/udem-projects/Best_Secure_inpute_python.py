##################      high security measures for input handling.    ########################

import re

def sanitize_input(input_value):
    # Remove any leading or trailing white spaces
    sanitized_input = input_value.strip()

    # Remove any special characters
    sanitized_input = re.sub(r'[^\w\s]', '', sanitized_input)

    # Ensure the input is within a certain length limit
    sanitized_input = sanitized_input[:100]

    return sanitized_input

def get_user_input():
    user_input = input("Enter your input: ")
    sanitized_input = sanitize_input(user_input)
    return sanitized_input

# Usage
user_input = get_user_input()
print("Sanitized input:", user_input)


