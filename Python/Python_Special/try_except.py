########################################################################################################################
print(f"\n")
title = " Try  Exeception ".upper()
print(title.center(44, "="))
print(f"\n")
########################################################################################################################
"""
-The [try] block lets you test a block of code for errors.
-The [except] block lets you handle the error.
-The [else] block lets you execute code when there is no error.
-The [finally] block lets you execute code, regardless of the result of the try- and except blocks.
"""

# Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")



# Try: In this example, the try block does not generate any error:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")






# Try to open and write to a file that is not writable:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")



  ########################################################################################################################
  print(f"\n")
  title = " throw an Eexception if condition occours".upper()
  print(title.center(44, "="))
  print(f"\n")
  ########################################################################################################################
"""
As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.
"""

# Raise an error and stop the program if x is lower than 0:
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")


#Raise a TypeError if x is not an integer:
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
