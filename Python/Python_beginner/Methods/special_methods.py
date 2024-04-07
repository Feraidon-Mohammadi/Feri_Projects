
# CLASS METHOD
# Methods associated with a class rather than instances of the class.
class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method")

MyClass.class_method()

########################################################################################

# Static Methods:
#Methods that don't access or modify class or instance state.
# Example of a static method
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")

MyClass.static_method()

########################################################################################

# Special Methods (Dunder Methods):
# Methods with double underscores, used for operator overloading.
# Example of a special method
class MySpecialClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MySpecialClass(self.value + other.value)

obj1 = MySpecialClass(5)
obj2 = MySpecialClass(10)
result = obj1 + obj2
print(f"Result value: {result.value}")


########################################################################################

# __str__ and __repr__:
#Used to provide a string representation of an object.
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass object with value: {self.value}"

    def __repr__(self):
        return f"MyClass({self.value})"


# i added self this parameters value
x = MyClass(value=22)
print(x)

########################################################################################

# __len__:

#Used to define the behavior of the len() function for an object.

class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


########################################################################################

#__getitem__ and __setitem__:
#Used for getting and setting values using square bracket notation.

class MyList1:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value



########################################################################################
# +++++++++++++++++++++++++ important method +++++++++++++++++++++++++++ #

#__iter__ and __next__:
#Used for making an object iterable.

class MyIterable:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration # ++++++++ wichtig ++++++++++ #


########################################################################################

#__eq__ and __ne__:
#Used for defining equality and inequality comparisons.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)


########################################################################################








########################################################################################







########################################################################################










