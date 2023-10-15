

person = "Megan"
coins = 3




print(f"\n" + person + "has" + str(coins) + "coins left.")

message = "\n%s has %s coins left ." % (person, coins)
print(message)


message = "\n{} has {} coins left .".format(person, coins)
print(message)


#switch position of inputs 
message = "\n{1} has {0} coins left .".format( coins, person)
print(message)


message = "\n{person} has {coins} coins left .".format( coins=coins, person=person)
print(message)



player = {"person":"jesicca", "coins":"3"}
message = "\n{person} has {coins} coins left .".format( **player)

print(message)

###################################################################################################################
print(f"\n")
title = " F strings ".upper()
print(title.center(44, "="))
print()
###################################################################################################################

# f-strings! This is the way


message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2 * 4} coins left."
print(message)



message = f"\n{person.lower()} has {coins} coins left."
print(message)


message = f"\n{player['person']} has {coins} coins left."
print(message)


##################################################################################################################
print(f"\n")
title = "F strings plus formatting options ".upper()
print(title.center(44, "="))
print()
##################################################################################################################



num = 10
message = f"\n2.25 times {num} is {2.25 * num:.2f}\n"
print(message)

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f" {num} divided by 3,42 is {num / 2.42:.2%}")


########################################################################################################################
print(f"\n")
title = "".upper()
print(title.center(44, "="))
print()
########################################################################################################################


user_input1= int(input("give a Numbers, integer: "))
user_input2 = input("give some numbers , int or double: ")
message = f"\n{user_input2}times {user_input1} is {12.34 * user_input1:.2f}"
print(message)



















