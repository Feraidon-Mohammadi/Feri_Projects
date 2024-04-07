
# Gesamte price
class Prices:
	def __init__(self, wasser , strom, miete, heitzung, price ):
		self.price = price
		self.wasser = wasser
		self.strom = strom
		self.miete = miete
		self. heitzung = heitzung
	
	def warning(self):
		if self.price >= 2000:
			print("Mahnung price ist so hoch")
			
			
class shulden(Prices):
	def __init__(self, wasser, heitzung, price ,nebenkosten, nachzahlung ):
		super().__init__(wasser, heitzung, price )
		self.nebenkosten = nebenkosten
		self.nachzahlung = nachzahlung
		
	def additonal(self):
		if self.nebenkosten == 1000:
			print(f"here is water{self.wasser} + {self.nebenkosten}")
			
		
		