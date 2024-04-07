import hashlib




password_hash = "112aa01926aebb65c5e09cc0a25ce2b5cff2ec5df0e9b123510db6753557ef5e5r2i"
sonder_zeich = "!§$%&/()=?"

with open(".\\Kursmaterialien\\data\\dictionary.txt", "r") as file :
	for line in file:
		word = line.strip()
		
		for char in sonder_zeich:
			x = word + char
			for char1 in sonder_zeich:
				xx = x + char1
				
				#print(xx)
			
		
		
				if hashlib.sha256(xx.encode()).hexdigest() == password_hash:
					print(f"congratulation ! you got it: {xx}")
					break
					
			if hashlib.sha256(x.encode()).hexdigest() == password_hash:
				print(f"congratulation ! you got it: {x}")
				break
				
		if hashlib.sha256(word.encode()).hexdigest() == password_hash:
			print(f"congratulation ! you got it: {word}")
			break