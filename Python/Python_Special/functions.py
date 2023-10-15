########################################################################################################################
print()
title = " fuctions without parameters".upper()
print(title.center(44, "="))
print()
########################################################################################################################


def my_function():
    print("add 2 numbers ")
my_function()



# adidtion function
num1 = int(input("Enter first Number: "))
num2 = int(input("Enter sercond Number: "))
def sum():

    print(f"first number + second number is = : {num1 + num2}")
sum()




# minus
def minus():
    print(f"first number + second number is = : {num1 - num2}")
minus()




# multiplication function
def multiplication1():
    print(f"first number * second number is = : {num1 * num2}")
    print(f"first number ** second number is = : {num1 ** num2}")
multiplication1()



# dividion function
def division():
    print(f"first number / second number is = : {num1 / num2}")
    print(f"first number // second number is = : {num1 // num2}")
division()

########################################################################################################################
print(f"\n")
title = " funcitons with parametes".upper()
print(title.center(44, "="))
print(f"\n")
########################################################################################################################

num1 = int(input("Enter first Number: "))
num2 = int(input("Enter sercond Number: "))


# adidtion function

def sum(num1, num2):
    print(f"first number + second number is = : {num1 + num2}")
sum(num1 , num2)




# minus
def minus(num1, num2):
    print(f"first number + second number is = : {num1 - num2}")
minus(num1, num2)




# multiplication function
def multiplication1(num1, num2):
    print(f"first number * second number is = : {num1 * num2}")
    print(f"first number ** second number is = : {num1 ** num2}")
multiplication1(num1, num2)



# dividion function
def division(num1, num2):
    print(f"first number / second number is = : {num1 / num2}")
    print(f"first number // second number is = : {num1 // num2}")
division(num1, num2)



########################################################################################################################
print(f"\n")
title = "".upper()
print(title.center(44, "="))
print(f"\n")
########################################################################################################################




# functions with return
eingabe1 = input("return function_of sum zahl1: ")
eingabe2 = input("return function_of sum zahl2: ")
def sum(eingabe1,eingabe2):
    return eingabe1 + eingabe2
    #print(f"first number + second number is = : {num1 + num2}")
result = sum(eingabe1, eingabe2)
print(f" here is result of return functiono: {result}")



















