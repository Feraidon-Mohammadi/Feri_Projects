# Funtions  inputs/functionality/output

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2



# special function called calc_function as parimeter
def calculate(calc_fuction, n1 , n2):
    return calc_fuction(n1, n2)

result1 = calculate(add,22, 4)
result2 = calculate(subtract,22, 4)
result3 = calculate(multiply,22, 4)
result4 = calculate(divide,22, 4)

print(f"add: {result1}\nsubtract: {result2}\nmultiply: {result3}\ndivide: {result4}")


########################################################################################################################

# Nested functions

def outer_fuction():
    print("i'm outer fuction")

    def nested_function():
        print("i'm inner fuction")

    nested_function()

outer_fuction()


########################################################################################################################
# return functions from another functions
print("\n###############################################################################\n")
def outer_fuction():
    print("i'm outer fuction")

    def nested_function():
        print("i'm inner fuction")

    return nested_function

inner_function = outer_fuction()
inner_function()  ########### it got nested function automatikally ##############























