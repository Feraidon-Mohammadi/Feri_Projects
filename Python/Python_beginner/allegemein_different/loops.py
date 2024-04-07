import  math

########################################################################################################################
print(f"\n")
title = " while Loop ".upper()
print(title.center(44, "="))
print(f"\n")
########################################################################################################################



value = 1
while value <= 10:
    print(value)
    if value == 5:
        break
    value +=1


value = 1
while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("value is nwo equal to "+ str(value))
    


########################################################################################################################
print()
title = " for loop ".upper()
print(title.center(44, "="))
print()
########################################################################################################################

liste_names = ["Dany", "Sara", "John", "Reza"]



for x in liste_names:
    print(x)


for x in "Mississippi":
    print(x)





for x in liste_names:
    if x == "Sara":
        break
    print(x)

"""

for x in liste_names:
    if x == "Sara":
        continue
        print(x)

"""


for x in range(4):
    print(x)


"""

for x in range(2,4):
    print(x)

"""

for x in range(2,4):
    print(x)





for x in range(1, 20, 4):
    print(x)
else:
    print("Glad you got it that\'s over!")



########################################################################################################################

liste_names = ["Dany", "Sara", "John", "Reza"]
liste_actions = ["codes", "eats", "reads", "sleeps"]

"""
for name in  liste_names:
    for action in liste_actions:
        print(name + " " + action +" ")


"""
for name in  liste_names:
    for action in liste_actions:
        print(name + " " + action +" ")











