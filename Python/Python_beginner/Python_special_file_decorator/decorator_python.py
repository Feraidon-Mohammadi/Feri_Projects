import time


# python Decorator function # used to add some small functionality to any function that we need

def delay_decorator(function):
    def wrapper_function():
        time.sleep(5)
        # Do somthing before
        function() # can be added multiple times
        #function()
        # Do somthing after
    return wrapper_function



def say_hello():
    print("hello without delay ")
say_hello()


def i_runing():
    print("im runing , but added without: @ sign of decorator but with delay")
#i_runing()

@delay_decorator
def say_bye():
    print("bye with delay ")
say_bye()

@delay_decorator
def say_greeting():
    print("how are u? again with delay ")
say_greeting()

#### ++++++++++++++  if didnt want to use @ decorators its alittle harder +++++++++++  ####
#if want to add decorator to a function without @ sign that is like this
decorator_function = delay_decorator(i_runing)
decorator_function()



