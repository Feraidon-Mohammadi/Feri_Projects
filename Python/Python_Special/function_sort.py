
list_element = [8, 3, 7, 5, 6, 12, 2, 1]


def sort_element(new_list):
    n = len(new_list)

    for i in range(n):
        for x in range(0, n - i -1): # start = 0   and stop = n-i and every step how far (step) = -1

            if new_list[x] > new_list[x + 1]:
                new_list[x], new_list[x + 1] = new_list[x +1], new_list[x]


    return new_list

f_list = sort_element(list_element)
print(f_list)













