# class methods

class Person:
	number_of_people = 0
	GRAVITY = -9.8
	
	def __init__(self, name):
		self.name = name
		Person.add_person()
	
	# class attribute after add every person this attribute will add nummber of people and its attribute
	# Person.number_of_people +=1
	
	@classmethod
	def number_of_people_(cls):
		return cls.number_of_people
	
	@classmethod
	def add_person(cls):
		cls.number_of_people += 1


p1 = Person("tim")
print(Person.number_of_people)

p2 = Person("jem")
print(Person.number_of_people)
print(Person.number_of_people_())

