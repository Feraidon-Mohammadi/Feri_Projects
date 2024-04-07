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



# print None if not True and not False
def sum(num1=0, num2=0): # to fix that we dont have not  so give to parameters 0 value so will be better than None
    if type(num1) is not int or type(num2) is not int:
        return 0
    return num1 + num2

total = sum(33, 4)
print(total)


# *args that mean we can add too many parameters ,when we dont know how many we need its so usefull
def multiple_items(*args):
    print(args)
    print(type(args))
    
multiple_items("dany", "johnny","sara") #output type is a tuple


# **kwargs  keywords arguments
def mult_named_item(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
mult_named_item(first = "dany",second = "johnny", last = "sara") # output is a Dictionary















