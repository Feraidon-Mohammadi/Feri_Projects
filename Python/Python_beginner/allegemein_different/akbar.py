
class cirCle:

	def __init__(self, shoaa):
		self.shoaa = float(input())
		self.pi = 3.14

	def ghotr(self):
		return self.shoaa * 2

	def mohit(self):
		return self.shoaa * self.pi * 2

	def masahat(self):
		return self.pi * self.shoaa ** 2

while True:
	try:
		while True:
			cir = cirCle("give a float Number: ")
			ghtr = cir.ghotr()
			mht = cir.mohit()
			msht= cir.masahat()
			print(f"Number Pi = {cir.pi}\ninput radius: {cir.shoaa}\nghotr: {ghtr}\nand mohit: {mht}\nand masahat: {msht}")
	except:
			print("please give a number not an string ")
########################################################################################################################



	
		
		
