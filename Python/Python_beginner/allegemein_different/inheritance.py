#Create a class named Person, with firstname and lastname properties, and a printname method:


# Note: The __init__() function is called automatically every time the class is being used to create a new object.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()






class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)




#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

#Example
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    #Add a property called graduationyear to the Student class
    self.graduationyear = 2019

#####################################################################
#In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects.
# To do so, add another parameter in the __init__() function:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    #Add a property called graduationyear to the Student class
    self.graduationyear = 2019

x = Student("Mike", "Olsen", 2019)


########################################################################################################################
#Add a method called welcome to the Student class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  #methode added
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)





























