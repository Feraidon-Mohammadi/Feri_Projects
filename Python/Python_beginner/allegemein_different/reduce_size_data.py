import sys


# Reduce or increase size of the created data
my_list = [i for i in range(100000)]
print(sum(my_list))
print(sys.getsizeof(my_list), "bytes")


my_generator = (i for i in range(100000))
print(sum(my_generator))
print(sys.getsizeof(my_generator), "bytes")





# set and get in dictionary
my_dict = {"item":"footbal", "price": 20.10}
count = my_dict.get("count", 0)
print(count)


count = my_dict.setdefault("count", 0)
print(count)
print(my_dict)






# hachable  count object
from collections import  Counter

myListf = [10, 10, 10 , 4, 7,   8 , 8  ,8 , 8, 8]
counter = Counter(myListf)

most_common1 = counter.most_common(1)
most_common2 = counter.most_common(2)
most_common3 = counter.most_common(3)

print("tuple created with first and plust second: ",most_common1)

print(most_common1[0])
print(most_common2[0][1])
print(most_common3[1][1])
print(most_common1[0][0])