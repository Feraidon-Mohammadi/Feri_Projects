

# Lambda functions are functions that we can use  as arguments  but so short function

#creaet a list with second elemets of the list
my_list1 = [(2, 5 ), (4, 5), (6, 3), (12, 45)]
new_list1 = list(map(lambda x: x[1] , my_list1))
print(new_list1)





#sort second element of the list
my_list3 = [(2, 7 ), (4, 5), (6, 3), (12, 45)]
new_list11 = sorted(my_list3, key = lambda x: x[1])
print(new_list11)




# sort elements with using if statement in lambda function
my_list2 = [2, 5, 4, 5,6, 3, 12, 45]

new_list=list(map( lambda x: "big" if x > 10  else "smal" , my_list2))
print(new_list)





# filter in lambda
# use % to divid in a number if = 0  than its true
my_list4 = [2, 4, 5, 7, 5, 14, 11, 3, 12, 45]
my_filter_list = list(filter(lambda x: x %2 == 0 , my_list4))
print(my_filter_list)

