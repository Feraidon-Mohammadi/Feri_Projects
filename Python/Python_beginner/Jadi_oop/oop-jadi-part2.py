class Computer:
	count = 0
	
	def __init__(self, ram, hard, cpu):
		Computer.count += 1
		self.ram = ram
		self.hard = hard
		self.cpu = cpu
	
	def value(self):
		return self.ram + self.hard + self.cpu
	
	#def cleanup(self):
	#	Computer.count -= 1
	
	# or this del to remove
	def __del__(self):
		Computer.count -= 1


class Laptop(Computer):
	#pass # that mean not any different ,it's the same as parents class
	def __init__(self, ram, hard, cpu, sie):
		super().__init__(ram, hard, cpu)
		self.size = sie
		
	def value(self):
		return super().value() + self.size
	

laptop1 = Laptop(16, 2, 4, 55)
print(laptop1.value())


pc1 = Computer(12, 2, 4)
print(pc1.value())
del pc1

pc2 = Computer(8, 4, 6)
print(pc2.value())
#pc2.cleanup()
