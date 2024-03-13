# sets , dictionary , tuple , list ,

line1 =      "***********************************"
line3 =      "*        Sets Collections         *"
line5 =      "***********************************"
print(line1)
print(line3)
print(line5)
space = f"\n"
########################################################################################################################

this_set = {"apple","banana","cherry","orage","coconute","ananas","mongo","watermelon","kiwi","lemon" }
print("x" in this_set) # output => false
print("banana" in this_set) #output => True

# unchangable(no replace)  and unordered(no sort,every time different place and no index or key)  and no duplicate values
# to access the certain items can convert to a list and  than can get elements by list[index]
# to check that a certain items to know is exist in set , can use if statement


find_fruit = "Which fruit are u looking for: "
print(find_fruit)
result = "apple"
#or
#result = str(input())
if result in this_set:
    print(result + " is in the list!")

    find_fruit = "Which fruit are u looking for again: "
    print(find_fruit)
    if result in this_set:
        result = "banana"
        #result = str(input())
        print(result + " Hier is what u needed")
    else:
        print(f" Im sorry ({result}) is not in the list! :(  ")
else:
    print( f" Im so sorry ({result}) is not in the list! :( ")

"""
############################################################################################
"""
this_set2 = {"apple", "banana", "cherry", "orage", "coconute", "ananas", "mongo", "watermelon", "kiwi", "lemon"}

for x in this_set2:
    place = "*"
    my_list = [this_set2]
    print(f"{place * 1}{x}")

    #for f in my_list:
        #print(f"{f}")
"""
#############################################################################################
"""
#add items to a Sets 
this_set3 = {"apple", "banana", "cherry", "orage", "coconute", "ananas", "mongo", "kiwi", "lemon"}

this_set3.add("pflaumen")
this_set3.add("apfel")
this_set3.add("madarine")
this_set3.add("wassermelone")
print(this_set3)

"""

"""
fruit_set = {"apple", "banana",  "orange", "lemon"}
color_set = {"Red", "Green","Blue", "White"}
# Add all  elements from this_set to another_set
#fruit_set.update(color_set)
#print(fruit_set)


street = "max street 33"
city = "Raconcity"
zipcode = "12345"

address = f"street: {street}, city: {city}, plz: {zipcode}"
# add just 1 element to another with forloop
fruit_set = {"apple", "banana",  "orange", "lemon", address}
color_set = {"Red", "Green","Blue", "White","Red"}

for red in color_set:
    fruit_set.add("red")

print(fruit_set)
print(color_set)

"""

##############################################################################################
# remove from set
"""
this_set4 = {"apple", "banana", "cherry", "orage", "coconute", "ananas", "mongo", "watermelon", "kiwi", "lemon"}
this_set4.remove("apple")
this_set4.remove("mongo")
this_set4.remove("kiwi")
print(this_set4)










##############################################################################################

line1 =      "******************************************"
line3 =      "*      List + Dictionary Collections     *"
line5 =      "******************************************"
print(line1)
print(line3)
print(line5)



########################################################################################################################
print()
title = "1-dictionary wit (dict) contstructor ".upper()
print(title.center(44, "="))
print()
########################################################################################################################



first_form_of_dictionary = {"key1":"value1","key2":"value2","key3":"value3"}
print(f"dictionary:> {first_form_of_dictionary}")

 # dictionary with a constructor
dictionary_constructor = dict(name="feri", nachname="moh")
print(f" dictionary with constructor:>  {dictionary_constructor}")



########################################################################################################################
print()
title = "2-access to dictionarys element".upper()
print(title.center(44, "="))
print()
########################################################################################################################


form_dic = {"key1":"value1","key2":"value2","key3":"value3","key4":"value4"}
print(f"length of the dictionary is: ({len(form_dic)}) elements ")

get_valiue= form_dic.get("key3")
print(get_valiue)

get_value_dic= form_dic["key1"]
print(get_value_dic)

#another way to get key
get_value_other_way = form_dic.get("key4")
print(get_value_other_way)

print(len(get_valiue))



########################################################################################################################
print()
title = "3-get all keys or values of dictionary".upper()
print(title.center(44, "="))
print()
########################################################################################################################



keys_of_dictionary = form_dic.keys()
print(keys_of_dictionary)

values_of_dictionary = form_dic.values()
print(values_of_dictionary)


########################################################################################################################
print(space *10)
title = "4-dictionary in a tuple".upper()
print(title.center(44, "="))
print(space)
########################################################################################################################



dic_elements ={"key1":"value1","key2":"value2","key3":"value3","key4":"value4"}
dictionary_tuple_list = dic_elements.items()
print(dictionary_tuple_list)


#check in dictionary
dic_elements2 ={"key1":"value1","key2":"value2","key3":"value3","key4":"value4"}

chk = "key2" in dic_elements2
chk2 = "key100000" in dic_elements2

while True:
    print(f"is in list: {chk}")

    if chk:
        print(f"not in list: {chk2}")
    else:
        print(f"is in list : {chk}")

    break


########################################################################################################################
print()
title = "5-chang values of a dictionary".upper()
print(title.center(44, "="))
print()
########################################################################################################################

dic_elements3 ={"key1":"value1","key2":"value2","key3":"value3","key4":"value4"}
dic_elements3["key2"] = "key999"
print(f"changed value key2 to key999: {dic_elements3}")




########################################################################################################################
print()
title = "6-add or remove in dictinary".upper()
print(title.center(44, "="))
print()
########################################################################################################################


dic_elements4 ={"key1":"value1","key2":"value2","key3":"value3","key4":"value4"}
#dic_elements4["key2"] = "key999" #changed element
dic_elements4.update({"added_key":"added_value"})# added elements
print(dic_elements4)

########################################################################################################################
print(space *15)
title = "7-dont copy Dictionary like this ".upper()
print(title.center(44, "="))
print()
########################################################################################################################

dic_names = {"ali":"rezai", "tom":"tamy", "rock":"rocky", "josh":"johnny"}
dic_kv = {"a": "1", "b": "2" , "c": "3"}
print(f"orginal dictionary : {dic_names}")
print(f"original dicationary: {dic_kv}")

print()
# create a reference its copy but not it destroy 1 of those lists
dic_kv = dic_names  # create a reference
print(f"after referenc Names : {dic_names}")
print(f"after reference alpha_number {dic_kv}")

print()

dic_kv["feri"] = "moh"

print(f"after referenc Names after add element: {dic_names}")
print(f"dic_num after add element: {dic_kv}")

print("Bad Copy!!! :(, we added element to number when u call names its added to number also to names so we dont ned;( ")


########################################################################################################################
print(space *10)
title = "8-correct copy dictionary elements".upper()
print(title.center(44, "="))
########################################################################################################################
dic_namens = {"ali": "rezai", "tom": "tamy", "rock": "rocky", "josh": "johnny"}
dic_numbers = {"a": "1", "b": "2" , "c": "3"}
print(f"dic_name original: {dic_namens}")
print(f"dic_number origianl: {dic_numbers}")
print()

# copy list
dic_numbers = dic_namens.copy()

print(f"dic_name after refereces: {dic_namens}")
print(f"dic_number after refereces: {dic_numbers}")

print()

dic_numbers["Megan"] = "Roy"

print(f"after referenc Names after added element: {dic_namens}")
print(f"dic_num after add element after add element: {dic_numbers}")

print("Good Copy!!!,u added element in number , and it is in just numbers ;)")
########################################################################################################################
print(f"\n")
title = "9-copy with constructor function".upper()
print(title.center(44, "="))
print()
########################################################################################################################
# or use the dict() constructor function
dic_name_number3 = dict(dic_numbers)
print(dic_name_number3)
print("this is a good copy !!! ;)")

########################################################################################################################
print(f"\n")
title = "10-Nested Dictionaris ".upper()
print(title.center(44, "="))
print(f"\n")
########################################################################################################################

#nested dictionary

# addresses
addresse_member1 = {
    "country": "china",
    "city": "chang",
    "street": "rox 22",
    "zipcod": "332544"
}
addresse_member2 = {
    "country": "usa",
    "city": "Chicago",
    "street": "old_str_22",
    "zipcod": "452344"
}
addresse_member3 = {
    "country": "Detuschland",
    "city": "koeln",
    "street": "berg_str_32",
    "zipcod": "556434"
}





# memebers
member1 = {
    "vor_name": "ali",
    "nach_name ": "akbari",
    "aga": "33",
    "birthday": "null",
    "address": addresse_member1
}
member2 = {
    "vor_name": "reza",
    "nach_name": "amiry",
    "age": "22",
    "bithday": "null",
    "address": addresse_member2
}
member3 = {
    "vor_name": "rock",
    "nach_name": "johnson",
    "age": "22",
    "bithday": "null",
    "address": addresse_member3
}

# addresses
addresses = {
    "country": "china",
    "city": "chang",
    "street": "rox 22",
    "zipcod": "332544"
}

# band of members
band = {

    "member1":member1,
    "member2":member2,
    "member3":member3
}

for memeber, name in band.items():
    print(f"Here is band info: {memeber}: {name}")

print()
print(f"complete band in a line: {band}")
print()
band_m1_v_name = band["member1"]["vor_name"]
band_m2_nach_name = band["member2"]["nach_name"]
band_m3_addres = band["member3"]["address"]
print(f"First Member name: {band_m1_v_name},\n"f"Second Member nach name : {band_m2_nach_name}, \n"f"Third Member address: {band_m3_addres},")
# or we can call our element like this




########################################################################################################################
print(space * 10)
title = "11-SETs mit constructor fuction".upper()
print(title.center(44, "="))
print()
########################################################################################################################

set_nummer = {1, 2, 3, 4, 5} #its a set

num_set2 = set((1, 2, 3, 4, 5)) # its a constructor_function set
print(set_nummer)
print(num_set2)
print(type(num_set2))

print()

# NO duplicate allowed
nums = {1, 2, 2 ,4 ,5}
print(nums)




#True is a dupe of 1 , False is a dupe of zero
nums = {1, True, 2 , False, 3, 4, 0}
print(nums)


nums = {7, 4, 6, 55, True,False,0,4, 3, 5, 3, 5, 59,12, 33,44}


elements_nums = nums.remove(4)
elements_nums = nums.add(122222)
elements_nums = nums.pop()
print(nums)


second_nums = {11,22,333,444,555,666}
nums.update(second_nums)
print(nums)
print(">>>>>>update method can be used for [SETs-list-dicthionary-tuple ]<<<<<< ")

########################################################################################################################
print(f"\n")
title = ("++++Merge two sets to create new set+++").upper()
print(title.center(44, "="))
print()
########################################################################################################################

one = {1, 2}
zweite_set = {3, 4}
three = {5, 6, 7}

mynew_set = one.union(zweite_set)
print(mynew_set)

my_third_set_new = mynew_set.union(three)
print(f"merged alle 3 sets in new : {my_third_set_new}")

########################################################################################################################
print(f"\n")
title = "<<<Get duplicate Elements>>>>".upper()
print(title.center(44, "="))
print(f"\n")
########################################################################################################################
# Merge 2 sets to creat a new set
one = {1, 2, 3, 4, 5, 6, 9}
two = {3, 4, 5, 7, 8}

drei_set = one.union(two)
print(f"(union) das ist dritte set verknupfte zwei sets and gibt aus dublicate werden einmal ausgeben :  {drei_set}")

# keep just duplicate from first_set and second_set
one = {1, 2, 3 }
two = {2, 3, 4 }
one.intersection_update(two)
print(f"new gleiche zaheln{one}")



# get all elemets without duplication numbers or elements
one = {1, 2, 3, 4}
two = {2, 3, 4, 5}
one.symmetric_difference_update(two)
print(f"keep elements whichs are not in first set and hich are not in  second set : {one}")

########################################################################################################################
print(f"\n")
title = "-----> list -set - dic- tuple- common or cuplicates <-----".upper()
print(title.center(140, "="))
print(f"\n")
########################################################################################################################

#ein list
liste1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,333]
liste2 = [1, 2, 3, 4, 5, 6, 7 ,8, 9,333]
# einfachst mögliche add zwei listen in eine liste
list3 = liste1 + liste2
print(f"(zeil 481) add zwei liste einfachste möglichkeit mit duplicate:  [[ List ]]------------->: {list3}")
print()

########################################################################################################################

#add 2 sets in a new set without duplicates
erste_set = {1, 2, 4, 5, 6, 7, 8, 8, 9,333}
zweite_set = {4, 5, 5, 6, 6,333}
dritte_set = erste_set | zweite_set
print(f"add 2 sets in a new set:  {{ Set }}---------------------->{dritte_set}")

# Set gemeinsamkeit
result = erste_set.union(zweite_set)
print(f"gemeinsam zahlen von 2 sets:  {{ Set }}-------------->{result}")

#Set duplicates löscht
duplicate_set = {333,1, 3, 2, 2, 333, 2, 5, 2, 4, 4, 6, 4 }
print(f"duplicat set wird gelöscht:  {{ Set }}---------------->{duplicate_set}")

########################################################################################################################

print()
tuple_duplicat = (333, 1, 11, 1, 4, 44, 333, 4)
print(f"duplicat set wird nicht gelöscht: ( Tuple )----------------->{tuple_duplicat}")

print()
dictionary_duplicat = {"feri": "moh", "feri": "moh", "333": "333","333": "333"}
print(f"duplicat dictionary wird gelöacht: dictionary =>  {{'key':'value'}}-------->{dictionary_duplicat}")






########################################################################################################################
# What will be printed?

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])

def myf():
    test=print("fi")
    return test
myf()


########################################################################################################################
#Which line of code will change the starting_dictionary to the final_dictionary?

starting_dictionary = {
    "a": 9,
    "b": 8,
}

final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}
starting_dictionary["d"] = 88
final_dictionary = starting_dictionary
print("start_dictionary: ",starting_dictionary)
























