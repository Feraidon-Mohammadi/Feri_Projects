import hashlib
#  %% timeit -r 10 -n 1

extra_char = "-!§%&/()=?`:;*'"
password_hash = "1e3bf495a62012e7caf5fdd25624605f"

with open(".\\Kursmaterialien\\data\\dictionary.txt", "r") as file:
	for line in file:
		word = line.strip()
		
		for char in extra_char:
			new_word = word + char
			
			
			if hashlib.md5(new_word.encode()).hexdigest().strip() == password_hash:
				print(word + char)
				break
				
print("Program beendet !!!")

