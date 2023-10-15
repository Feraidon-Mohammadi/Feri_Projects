class Device:
	count = 0
	def __init__(self, ip, mac, name):
		self.ip = ip
		self.mac = mac
		self.name =name
		
		# result = ping the devicce
		result = True
		if result:
			self.status = "active"
		else:
			self.status = "unknow"
			
	def get_status(self):
		return self.status #return result  based on ping results for self.ip
	

class TV(Device):
	def turn_on(self):
		# connect to self.ip and turn on
		print(f"Turning on the TV at {self.ip}")
		
	def turn_off(self):
		# connect to self.ip and turn off
		print(f"Turning off the TV at {self.ip}")
		
		
class Thermo(Device):
	def get_degree(self):
		# Implement the logic to get the temperature reading from self.ip
		print(f"Reading temperature from {self.ip}")
		return 25  # Replace this with the actual temperature reading
	
	
class SmartTV(TV):
	def turn_on(self):
		# Implement the specific logic to turn on the Smart TV using self.ip
		print(f"Turning on the Smart TV at {self.ip}")
		
tv1 = TV("192.168.1.100", "00:11:22:33:44:55", "Living Room TV")
thermo1 = Thermo("192.168.1.200", "00:AA:BB:CC:DD:EE", "Living Room Thermostat")
smart_tv1 = SmartTV("192.168.1.101", "00:11:22:33:44:56", "Smart TV")

print(tv1.get_status())
tv1.turn_on()
tv1.turn_off()

print(thermo1.get_status())
print(thermo1.get_degree())

smart_tv1.turn_on()