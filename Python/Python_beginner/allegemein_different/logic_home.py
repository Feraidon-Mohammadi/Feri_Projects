import random
from itertools import count




list_element = [8, 3, 7, 5, 6, 12, 2, 1]


def sort_element(new_list):
	n = len(new_list)
	
	for i in range(n):
		for x in range(0, n - i - 1):  # start = 0   and stop = n-i and every step how far (step) = -1
			
			if new_list[x] > new_list[x + 1]:
				new_list[x], new_list[x + 1] = new_list[x + 1], new_list[x]
	
	return new_list


f_list = sort_element(list_element)
print(f_list)

########################################################################################################################
print()
title = " random from list  in new list ".upper()
print(title.center(80, "="))
print()
########################################################################################################################

def random_chose():
	list_word = ["feri", "smay", "meys", "shafi"]
	chosen_word = []
	while True :
		f =random.choice(list_word)
		chosen_word.append(f)
		
		return chosen_word
x_func = random_chose()
print(x_func)


########################################################################################################################
print()
title = " fibbonacci ".upper()
print(title.center(80, "="))
########################################################################################################################


# finbonacci
a = 0
b = 1
fib_list = [a , b]
user_input = int(input("Please give a Number: "))

def fibonac(user_input):
	ln = user_input
	
	for i in range(2, ln):
		next_fib = fib_list[i - 1] + fib_list[i-2]
		
		fib_list.append(next_fib)
		
		
	return fib_list
func_f= fibonac(user_input)
print(func_f)


########################################################################################################################
print()
title = "palinderom words ".upper()
print(title.center(80, "="))
print()
########################################################################################################################

list_words = ["work", "mum", "brothe", "sys", "aunt", "father", "roooor", "alot"]
new_w_list =[]
def polinderom():
	
	
	def is_polinderom(index):
		return index == index[::-1]
	
	
	for index in list_words :
		if is_polinderom(index):
			new_w_list.append(index)
		
	return new_w_list

polind_func = polinderom()
print(polind_func)

########################################################################################################################
print()
title = "easy way palinderom".upper()
print(title.center(80, "="))
print()
########################################################################################################################

list_words_2 = ["work", "mum", "brothe", "sys", "aunt", "father", "roooor", "alot", "kook"]
new_w_list_2 = []

def polinderom():
	for index in list_words_2:
		if index == index[::-1]:
			new_w_list_2.append(index)
	
	return new_w_list_2
polind_func = polinderom()
print(polind_func)

########################################################################################################################
print(f"\n")
title = "Prime Numbers".upper()
print(title.center(80, "="))
print()
########################################################################################################################

prime_list =[]
user_in = int(input("give max Number to get all prime numbers: "))
# prime conditions
def is_prime(every_number_in_loop):
	if every_number_in_loop <= 1:
		return False
	for i in range(2, int(every_number_in_loop ** 0.5) + 1):
		if every_number_in_loop % i == 0:
			return False
	return True

def prime_number(user_in):
	for i in range(2,user_in):
		if is_prime(i):
			prime_list.append(i)
	return prime_list
prime_func = prime_number(user_in)
print(prime_func)

"""

########################################################################################################################
print(f"\n")
title = " factorial Nummbers or words".upper()
print(title.center(80, "="))
print()
########################################################################################################################

"""
# abcdef
str_list = []
user_input_word = str(input("Type some Alphabets to geuss how many name or words can be create without repeats: "))
user_in_div = input("slice in how many words: ")
result= []
final_result = []
def factorial_n(user_input_word, user_in_div):
	i = 0
	for i in user_input_word:
		str_result = str_list.count(i)
		str_list.append(str_result)
		formule = user_in_div(user_in_div - i)
		final_result.append(formule)
		
		for j in user_in_div:
			answer = j// j-i
			result.append(answer)
		return result
	return str_list
fac_func = factorial_n(user_input_word, user_in_div)
print(fac_func)







user_input_word2 = str(input("Type some Alphabets to geuss how many name or words can be create without repeats: "))
char_count = []

def firs_factor(user_input_word2):
	
	for char in user_input_word2:
		found = False
		
		for item in char_count:
			if item[0] == char:
				item[1] += 1
				found = True
				break
			if not found:
				char_count.append([char, 1])
			
	return char_count
x = firs_factor(user_input_word2)
print(x)



"""

def factorial_n(user_input_word, user_in_div):
		
		for j in user_in_div:
			answer = j // j - i
			result.append(answer)
		return result
	return str_list


fac_func = factorial_n(user_input_word, user_in_div)
print(fac_func)

"""









