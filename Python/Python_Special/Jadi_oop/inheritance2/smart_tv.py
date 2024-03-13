from Jadi_oop.inheritance.tv import TV


class SmartTV(TV):
	def turn_on(self):
		# Implement the specific logic to turn on the Smart TV using self.ip
		print(f"Turning on the Smart TV at {self.ip}")
