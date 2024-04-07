"""
Exercise 4: Create a Rectangle Class
Create a Rectangle class with attributes length and width.
Implement methods to calculate the area and perimeter of the rectangle.
"""
class Rectangle:
	def __init__(self, length, width):
		self.length =length
		self.width=width
		
	
	def calculate_area(self):
		x = self.length * self.width
		print(f"Area size is: {x}")
		
	
	def calculate_scop(self):
		f = self.length * 2 + self.width * 2
		print(f"scop size: {f}")

instance_calss = Rectangle(4,6)
instance_calss.calculate_area()
instance_calss.calculate_scop()

############################################### second rectangle #######################################################
class Rectangl:
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def calculate_area(self):
		area = self.length * self.width
		return area

	def calculate_perimeter(self):
		perimeter = 2 * (self.length + self.width)
		return perimeter

# Example usage:
rectangle1 = Rectangl(length=6, width=4)
area1 = rectangle1.calculate_area()
perimeter1 = rectangle1.calculate_perimeter()

print(f"Rectangle 1 - Area: {area1}, Perimeter: {perimeter1}")

rectangle2 = Rectangl(length=2, width=3)
area2 = rectangle2.calculate_area()
perimeter2 = rectangle2.calculate_perimeter()

print(f"Rectangle 2 - Area: {area2}, Perimeter: {perimeter2}")
