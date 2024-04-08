import hashlib


password_hash = "oeiwewf8euw9889rz23r32hr9822h9f23rf2983f"

# # md5 password
# x = hashlib.md5("fereydoun".encode())
# f = x.hexdigest()
# print(f)
#
#
# x2 = hashlib.sha3_512("fereydoun".encode())
# f2 = x2.hexdigest()
# print(f2)

with open(".\\Kursmaterialien\\data\\dictionary.txt" , "r") as file :
	for line in file:
		word = line.strip()
		
		if hashlib.md5(word.encode()).hexdigest() == "9e083ec666c9f3db044bb7c381640227":
			print(f"Das password war: {word}\n")
			break
print("Program beendet !!!")
	
		
