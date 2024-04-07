def decorator_function(func):
    def wrapper(a, b):
        result = func(a, b)
        # Multiply the result by 5
        result *= 5
        return result
    return wrapper

@decorator_function
def sum_function(a, b):
    return a + b

# Example usage:
result = sum_function(2, 3)
print(result)





####################################################### Decorator ######################################################
def decorator_function_multiple(method):
    def wrapper_function(self, *args , **kwargs):
        result = method(self, *args , **kwargs)
        # divide result by 4
        result /= 4
        return result
    return wrapper_function  # return the function without ()


class MyClassName:

    def __init__(self, variable, another_variable, a, b):
        self.a = a
        self.b = b
        self.variable = variable
        self.another_variable = another_variable




    def hello(self):
        return "hello"

    @decorator_function_multiple
    def multiply(self, a, b):
        print(f"Original multiply function: {a * b}")
        return a * b

    def divide(self, a, b):
        print(f"Divide function: {a / b}")
        return a / b

    @decorator_function_multiple
    def som_function(self, a, b):
        return a + b

object_of_class = MyClassName(1, 2, 3,4)

# Call multiply with decorator
result = object_of_class.multiply(4, 6)
print(result)

# Call som_function with decorator
object_of_class.som_function(4, 22)



##############################################  cal it undirekt  #######################################################
#
# class MyClassName2:
#
#     def __init__(self, variable, another_variable):
#         self.variable = variable
#         self.another_variable = another_variable
#
#
#     def decorator_function_multiple(self, function):
#         def wrapper_function(self, a, b):
#             if a + b >= 10:
#                 x = a * b
#                 print(x)
#             return function(self, a, b)  # Return the result of the wrapped function
#         return wrapper_function  # Return the function without ()
#
#
#     def hello(self):
#         return "hello"
#
#
#     @decorator_function_multiple
#     def some_function(self, a, b):
#         return a + b
#
# object_of_class = MyClassName2(2, 8)
#
# # Call the original method directly
# result_direct = object_of_class.some_function(4, 22)
# print(result_direct)
#




"""
# example : 


1- Methods are functions with parimeter or without parimeter and can be callabe with create an object of the function.
2- Methods can be nested and can be call from outer functions with creating an object and apss in the function and and
    return object as function and to use functions in class with can pass variables trough
    instans variable sefl for example: def function(self).

3- Class with Uppercase to atleas 1 character upperCase, can be inharit from another class
4- for specific project usually need centainly variables, to initialize the project, and for initialization need to create a construtor.
5- for specific project, to initialize need to use:  def __init__.(self, *args):  # can be added multiple vairables for future.

6- or can be use with parimeter when we no we dont add more :  def __init__(self, avarable, another_variable):
                                                                            self.variabel = variable
                                                                            self.anther_variable = anther_variable

7- class in python can be return valuse to return values or pass in to the functions or class some values 
    for specific defined variable can be pass in to end of the function return 
    like : some_function(variable= , another_variable= )

    or can just give the values in to the primeter positon like : some_function( 3 , 22) 
    













"""