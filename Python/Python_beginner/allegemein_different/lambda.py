
########################################################################################################################
############### Lambda are functions that can be used  as (1) arguments in funcs  but so short function ################
########################################################################################################################

"""
Lambda functions in a list can be used with:

#1 Map Function: Transform each element of a list.
#2 Filter Function: Select elements based on a condition.
#3 Sort Function: Customize sorting criteria.
#4 List Comprehensions: Create a new list.
#5 Reduce Function (from functools): Accumulate values in a list.
#6 Any and All Functions: Check if any or all elements satisfy a condition.
"""

# 1 # Map Function:
# Purpose: Applies a given function to all items in an input list (or other iterable).
# Syntax: map(function, iterable)
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)



# 2 # Filter Function:
# Purpose: Filters elements from an iterable based on a function that returns True or False.
# Syntax: filter(function, iterable)
numbers = [1, 2, 3, 4, 5, 6, 7,8, 5, 4, 6, 7]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)



# 3 # Sort Functioin
# Purpose: Sorts elements of a list based on a custom key.
# Syntax: list_name.sort(key=lambda x: expression)
# list_name: The name of the list you want to sort.
# .sort: The method used to sort the list in-place.
# key: Parameter specifying a function (lambda function) to extract a sorting key.
# lambda x: expression: Lambda function defining the sorting key for each element x in the list.
my_list = [(1, 2), (4, 1), (3, 5), (2, 8)]
my_list.sort(key=lambda x: x[1])  # Sort based on the second element of each tuple
print(my_list)



# 4 # List Comprehension:
# Purpose: Concise way to create lists using a single line of code.
# Syntax: [expression for item in iterable if condition]
numbers = [1, 2, 3, 4]
squared2 = [x**2 for x in numbers]



# 5 # Reduce Function (from "functools"):
# Purpose: Successively applies a binary function to the items of an iterable, reducing it to a single accumulated value.
# Syntax: functools.reduce(function, iterable[, initializer])
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(f"Product: {product}")



# 6 # Any and All Functions in lambda :
# Purpose: Check if any or all elements in an iterable satisfy a condition.
# Syntax:
# any(iterable): Returns True if at least one element in the iterable is True. Equivalent to or-ing all the elements.
# all(iterable): Returns True if all elements in the iterable are True. Equivalent to and-ing all the elements.
# You can use lambda to define the condition for checking.
numbers123 = [1, 2, 3, 4, 5, 6]
numbers1234 = [11, 22, 33, 44, 55, 66] # for test , (any) can have just 1 parimeter ,so i created an object that
# Check if any element is even
x = lambda x: x % 2 == 0, numbers123
has_even = any(x)
print(f"Any lambda: {has_even}")  # Output: True

numbers11 = [1, 2, 3, 4, 5, 6]
# Check if all elements are greater than zero
f = lambda x: x > 0, numbers11
all_greater_than_zero = all(f)
print(f"All lambda {all_greater_than_zero}")  # Output: True





# 6 # Any and All Functions:
# Purpose:
# any(): Returns True if at least one element in the iterable is True.
# all(): Returns True if all elements in the iterable are True.
# Syntax: any(iterable) and all(iterable)
numbers = [True, False, True, True]
has_true = any(numbers)
all_true = all(numbers)




########################################################################################################################


# create a list with second elements of the list
my_list1 = [(2, 5), (4, 5), (6, 3), (12, 45)]
new_list1 = list(map(lambda x: x[1], my_list1))
print(new_list1)

########################################################################################################################

# sort second element of the list
my_list3 = [(2, 7), (4, 5), (6, 3), (12, 45)]
new_list11 = sorted(my_list3, key=lambda x: x[1])
print(new_list11)

########################################################################################################################

# sort elements with using if statement in lambda function
my_list2 = [2, 5, 4, 5, 6, 3, 12, 45]

new_list = list(map(lambda x: "big" if x > 10 else "smal", my_list2))
print(new_list)

########################################################################################################################

# filter in lambda
# use % to divid in a number if = 0  than its true
my_list4 = [2, 4, 5, 7, 5, 14, 11, 3, 12, 45]
my_filter_list = list(filter(lambda x: x % 2 == 0, my_list4))
print(my_filter_list)

########################################################################################################################

# an example lambda in tkinter for a button
"""
button_add = Button(frame, text="Submit", width=35, command=lambda :[display_warning(), save_data()])
button_add.grid(row=4, column=1, columnspan=3)
"""

########################################################################################################################

add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

########################################################################################################################

# Sorting a List of Tuples based on the second element:
points = [(1, 2), (3, 1), (5, 4), (2, 0)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)

########################################################################################################################

# filtering
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

########################################################################################################################

# mapping
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

########################################################################################################################

# lambda with using MAX
find_max = lambda x, y: x if x > y else y
print(find_max(5, 8))  # Output: 8

########################################################################################################################

# sort dictionary
dictionary = {'apple': 5, 'banana': 2, 'orange': 8}
sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1]))
print(sorted_dict)

########################################################################################################################

# calculate
power = lambda x, n: x ** n
print(power(2, 3))  # Output: 8

########################################################################################################################

# lambda with map and filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
transformed_numbers = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
print(transformed_numbers)

########################################################################################################################

# with reduce
from functools import reduce
product3 = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(product3)  # Output: 24

########################################################################################################################

# with expression condition
greater = lambda x, y: x if x > y else y
print(greater(5, 3))  # Output: 5

########################################################################################################################

# lambda in to a functions
def apply_operation(operation, x, y):
    return operation(x, y)

result = apply_operation(lambda a, b: a + b, 3, 4)
print(result)  # Output: 7

########################################################################################################################

# lambda with sort and revers
names = ['Alice', 'Bob', 'Charlie', 'David']
sorted_names = sorted(names, key=lambda x: len(x), reverse=True)
print(sorted_names)

########################################################################################################################

# lambda with creating Dynamically funcitons
def power_function(n):
    return lambda x: x ** n


square = power_function(2)
cube = power_function(3)
print(square(4))  # Output: 16
print(cube(3))  # Output: 27

########################################################################################################################

# extracting elements from tuple
points = [(1, 2), (3, 1), (5, 4), (2, 0)]
get_second_element = lambda x: x[1]
second_elements = list(map(get_second_element, points))
print(second_elements)

########################################################################################################################

# Lambda in list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [(lambda x: x ** 2)(num) for num in numbers]
print(squared_numbers)

########################################################################################################################

# partial function application
from functools import partial
# Using partial to create a specialized function
power_of_two = partial(lambda x, n: x ** n, n=2)
print(power_of_two(3))  # Output: 9

########################################################################################################################

# Sorting a list of tuples based on multiple criteria using lambda
data = [('apple', 5), ('banana', 2), ('orange', 8)]
sorted_data = sorted(data, key=lambda x: (len(x[0]), x[1]))
print(sorted_data)

########################################################################################################################

# Checking if any element in a list is even
# has_even = any(lambda x: x % 2 == 0, [1, 3, 5, 2, 7]) ## its not worked
has_even1 = any(x % 2 == 0 for x in [1, 3, 5, 2, 7])
print(has_even1)  # Output: True

has_even = any(map(lambda x: x % 2 == 0, [1, 3, 5, 2, 7]))
print(has_even)  # Output: True

# Checking if all elements in a list are odd
all_odd = all(map(lambda x: x % 2 != 0, [1, 3, 5, 7]))
print(all_odd)  # Output: True

########################################################################################################################









########################################## old lamdas ###########################################################
# Lambda functions are functions that we can use  as arguments  but so short function

#create a new list with second elemets of the list
my_list1 = [(2, 5 ), (4, 5), (6, 3), (12, 45)]
new_list1 = list(map(lambda x: x[1] , my_list1))
print(new_list1)





#sort second element of the list
my_list3 = [(2, 7 ), (4, 5), (6, 3), (12, 45)]
new_list11 = sorted(my_list3, key = lambda x: x[1])
print(new_list11)





# sorte complex iterables with sorted()
data = (3, 5, 1 ,10, 8, 7)
sorted_data = sorted(data, reverse=True)
print(sorted_data)

data2 = [{"name":"Max", "age":6, "employeeID":"53FAt"},
         {"name":"Lisa", "age": 12,"employeeID":"43FAt"},
         {"name":"Roy", "age":22,"employeeID":"3FFAt"}]
sorted_data1 = sorted(data2, key=lambda x: x["age"])
sorted_data2 = sorted(data2, key=lambda x: x["name"])
sorted_data3 = sorted(data2, key=lambda x: x["employeeID"])
print("sorted by age: ",sorted_data1)
print("sorted by name: ",sorted_data2)
print("sorted by id : ",sorted_data3)







# sort elements with using if statement in lambda function
my_list2 = [2, 5, 4, 5,6, 3, 12, 45]

new_list=list(map( lambda x: "big" if x > 10  else "small" , my_list2))
print(new_list)





# filter in lambda
# use % to divid in a number if = 0  than its true
my_list4 = [2, 4, 5, 7, 5, 14, 11, 3, 12, 45]
my_filter_list = list(filter(lambda x: x %2 == 0 , my_list4))
print(my_filter_list)

