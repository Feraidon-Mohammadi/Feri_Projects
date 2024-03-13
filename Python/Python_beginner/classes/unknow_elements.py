# eval() dangerous code dont use in project because of security expression
user_input = input("Enter a Python expression: ")

# Get input from the user
try:
    # Use eval to evaluate the input
    result = eval(user_input)

    # Print the result
    print("Result:", result)
except Exception as e:
    print("Error:", e)


