def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
        for i in a_list:
            third_item = i * 3

            b_list.append(third_item)
        print(b_list)

    print(b_list)
mutate([1,2,3,5,8,13])
