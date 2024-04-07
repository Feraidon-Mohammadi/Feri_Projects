#from itertools import batched # it's working with pyton 3.12.0 v
batched = "to remove unknow parameters i added it to a variable should remove this line complett"
# change list elements with a tuples of 3 elents  in python 3.12v
#data: list[int] = [1, 2 ,3, 4, 5, 6, 7, 8, 9]
#batch: batched = batched( data, 3 )
#print(list(batch))








# replace acces elements
my_list = [1, [1, 2, 3,], ["hello", "hi", 10] , 100]
my_list[2][0] = "python"
print (my_list)



my_list1 = str(my_list)
mylist =my_list1.replace("hi", "python")
print(mylist)




my_list2 = [1, [1, 2, 3,], ["hello", "hi", 10] , 100]
my_list2[3]= "feri100"
print(my_list2)