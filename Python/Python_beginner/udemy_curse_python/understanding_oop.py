#In class1.py:
class Class1:
    def method1(self):
        print("Method 1 from Class1")
	    
	    
#In class2.py:
class Class2:
    def method2(self):
        print("Method 2 from Class2")
	    
	    
#In class3.py:
class Class3:
    def method3(self):
        print("Method 3 from Class3")
	    
	    
#In class4.py:
class Class4:
    @staticmethod
    def method4():
        print("Method 4 from Class4")
	    
	    
	    
	    
"""
#In your main Python file:

from class1 import Class1
from class2 import Class2
from class3 import Class3
from class4 import Class4

# Create instances of the classes
obj1 = Class1()
obj2 = Class2()
obj3 = Class3()

# Call the methods from the instances
obj1.method1()
obj2.method2()
obj3.method3()

# Call a static method from Class4 directly
Class4.method4()
"""