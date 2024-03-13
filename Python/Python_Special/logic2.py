



# finbonacci

a = 0
b = 1
fib_list = [a, b]
user_input = int(input("chose a Number and Type it here: "))


def fibonac(user_input):
    ln = (user_input-1)
    result = a + b

    for i in range(0, ln -1 ):
        fib_list.append(result )

        for j in range(result -a, ln -1 -1):

            new_res = result + j - fib_list[0]
            fib_list.append(new_res)



            new_res +=1


        return fib_list
    return fib_list


func_f = fibonac(user_input)
print(func_f)
