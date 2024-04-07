class Stundent:
	def __init__(self, name, age , grade):
		self.name = name
		self.age = age
		self.grade= grade
		
		
	def get_grade(self):
		return self.grade
	
	
class Course:
	def __init__(self, name , max_students):
		self.name= name # class attributes
		self.max_stundents = max_students # class attributes
		self.students = [] # class attributes
		
		
	def add_student(self, student):
		if len(self.students) < self.max_stundents:
			self.students.append(student)
			return True
		return False
	
	
	def get_average_grade(self):
		value = 0
		for student in self.students:
			value += student.get_grade()
	
		return value / len(self.students)
	
s1 = Stundent("Tim", 19 , 88)
s2 = Stundent("Roy", 29 , 84)
s3 = Stundent("Magi", 25 , 98)

course = Course("Science", 2 )
course.add_student(s1)
course.add_student(s3)

print(course.students[0].name)
print(course.add_student(s2))
print(course.get_average_grade())

########################################################################################################################
# useing methods as attributes

class MyClass:
	def method_one(self):
		return "This is method one"

	def method_two(self):
		return "This is method two"

my_object = MyClass()

# Using methods as attributes
my_object.attribute_one = my_object.method_one
my_object.attribute_two = my_object.method_two

# Calling methods via attributes
result_one = my_object.attribute_one()
result_two = my_object.attribute_two()

print(result_one)
print(result_two)
