import random


########################################################################################################################
print()
title = " from first list to new list add random items ".upper()
print(title.center(88, "="))
print()
########################################################################################################################

def my_random():
	word_list = ["advark", "baboon", "camel"]
	new_list = []
	for x in word_list:
		randx = random.choice(word_list)
		new_list.append(randx)

	return new_list
call_func = my_random()
print("new List: ", call_func)




########################################################################################################################
print()
title = " add chars of one elements of the list to another list".upper()
print(title.center(88, "="))
print()
########################################################################################################################

def my_random():
	word_list = ["advark", "baboon", "camel"]
	new_list = []
	randx = random.choice(word_list)
	for rand in randx:
		new_list.append(rand)


	return new_list
call_func = my_random()
print("new List: ", call_func)





########################################################################################################################
print(f"\n")
title = " add pick just 1 element and add it to new list but random  ".upper()
print(title.center(88, "="))
print()
########################################################################################################################

word_list = ["advark", "baboon", "camel"]
new_list = []
def ran_func():
	rand = random.choice(word_list)
	new_list.append(rand)

	return  new_list

my_func = ran_func()
print(my_func)



########################################################################################################################
print(f"\n")
title = " pick up from the list just one item random  ".upper()
print(title.center(88, "="))
print(f"\n")
########################################################################################################################

word_list2 = ["advark", "baboon", "camel"]
def ran_func():
	rand = random.choice(word_list2)
	return rand

my_func = ran_func()
print(my_func)






"""
list = []
nl = new_list.append(index)
return nl
"""
# it is not working because append just modified the list and it doesn't have any value
# nl  is a variable but it cant have value becuase append
########################################################################################################################
print(f"\n")
title = " sort function not completted ".upper()
print(title.center(44, "="))
print(f"\n")
########################################################################################################################

list_element = [8, 3, 7, 5, 6, 12, 2, 1]
first= list_element[0]
second = list_element[1]
double_list = []
first_second = list_element[first,second]
def sort_element():
	for every in first_second:
		if first >= second :
			double_list.append(second)
			list_element.remove(first_second)

		else:
			double_list.append(first)
			list_element.remove(first_second)

		for every in first_second:
			if first >= second:
				double_list.append(second)
				list_element.remove(first_second)

			else:
				double_list.append(first)
				list_element.remove(first_second)



	return double_list
func_sort=sort_element()
print(func_sort)



















"""
if __name__ == "__main__":
	my_random()
	#op1 = my_random()
	#print(op1)
"""