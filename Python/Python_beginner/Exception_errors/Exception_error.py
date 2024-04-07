
"""
x = int(input("x: ")) # a number
y = int(input("y: ")) # assume 0
divide = x / y
print(divide)# output will be an error zero division error
"""

# to fix it using try except
"""
try:
	x = int(input("x: "))  # a number
	y = int(input("y: "))  # assume 0
	divide = x / y
	print("value of x / 0  is: ")

except ZeroDivisionError:
	print("ZeroDivisionError")
	y = int(input("y: "))
	divide = x / y
	print(divide)
	
except ValueError:
	print("1ValueError!!!")
	
except:
	print("Unkown Error!")
	
print("End!!")

"""
# or fix so that ,  both errors doing the same thing ,
try:
	x = int(input("x: "))  # a number
	y = int(input("y: "))  # assume 0
	divide = x / y
	print("value of x / y  is = ", divide)
	print("value of x / y  is = ", divide) # name false

except (ZeroDivisionError, ValueError):
	print("Error: ")
	x = int(input("x: "))
	y = int(input("y: "))
	divide = x / y
	print(divide)
except NameError:
	print("NameError")
except:
	print("Unkown Error!")
else:
	print("End!!")


#################################################################################
#
try:
	x = int(input("x: "))  # a number
	y = int(input("y: "))  # assume 0
	divide = x / y
	print("value of x / y  is = ", divide)
	if y == 10:
		raise ValueError("haahahh Error!")

except (ZeroDivisionError, ValueError):
	print("Error: ")
	x = int(input("x: "))
	y = int(input("y: "))
	divide = x / y
	print(divide)
except NameError:
	print("NameError")
except:
	print("Unkown Error!")
else:
	print("End!!")
finally:        # this one it is a forced option that should be excecute anyway
	print("*" * 20 )
	