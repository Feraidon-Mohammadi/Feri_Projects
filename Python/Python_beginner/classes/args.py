def add(*args):
    print(args[1])

    sum1 = 0
    for n in args:
        sum1 += n
    return sum1


print(add(2, 4, 5, 6, 6, 7, 7, 7, 7))


def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print("this is the key: "+ key+ "\n")
        print("this is the value: ", value, "\n")


calculate(add=3, multiply=5)


def calculate2(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate2(4,add=3, multiply=5)


# special args
def all_different(a, *args, **kwargs):
    print(a, args, kwargs)


all_different(2,4, 5, 6, 3, 4, f=23, j=99)



