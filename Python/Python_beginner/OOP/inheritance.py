class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print(f"i am {self.name} and i am {self.age} years old")
		
	def speak(self):
		print("I don't  know  what i say")

class Cat(Pet):
	def __init__(self,name, age,  color):
		super().__init__(name, age)
		self.color = color
		
		
	def speak(self):
		print("meow")
	
	def show(self):
		print(f"i am {self.name} and i am {self.age} years old and im {self.color}")
	
	
class Dog(Pet):
	def speak(self):
		print("bark")
		


class Fish(Pet):
	pass



p = Pet("Tim", 19 )
p.show()

c = Cat("Bill", 34, "green")
c.show()

d = Cat("jill", 23, "blue")
d.speak()

