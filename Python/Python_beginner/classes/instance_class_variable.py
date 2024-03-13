########################################################################################################################
print()
title = " when functions are in same file to use main ".upper()
print(title.center(44, "="))
print()
########################################################################################################################


def function_one():
    print("This is function one.")


def function_two():
    print("This is function two.")


if __name__ == "__main__":
    print("This is the main program.")
    function_one()
    function_two()
    # You can include more code here as needed.


########################################################################################################################
print()
title = " using functions in main method if functions are in a class ".upper()
print(title.center(44, "="))
print()
########################################################################################################################


class MyClass:

    def method_one(self):
        print("Method one")

    def method_two(self):
        print("Method two")


if __name__ == "__main__":
    my_instance = MyClass()  # Create an instance of the class
    my_instance.method_one()  # Call methods of the class
    my_instance.method_two()


########################################################################################################################
print(f"\n")
title = "Assume you have a module named my_module.py containing a class with functions:".upper()
print(title.center(44, "="))
print()
########################################################################################################################


# my_module.py

class MyClass:
    def method_one(self):
        return "Method one result"

    def method_two(self):
        return "Method two result"


########################################################################################################################
print(f"\n")
title = "Now, in your main script, you can import the module and use the class and its functions:".upper()
print(title.center(44, "="))
print()
########################################################################################################################

# import my_module

if __name__ == "__main__":
    # my_instance = my_module.MyClass()  # Create an instance of the class
    result1 = my_instance.method_one()  # Call methods of the class
    result2 = my_instance.method_two()

    print(result1)  # Output: Method one result
    print(result2)  # Output: Method two result










