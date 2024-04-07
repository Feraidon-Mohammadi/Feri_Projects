#!/usr/bin/python3

password_hash = "$6$bVtoNJr/GHPs7R$i7Ip5frU9wEfPfGhFGE2w6CkdTpL21zQ2zRbZyR51KkFilzOf8prHxhxpiDzuxRhS8/TZyQ04t25hDXOajIl7."

import crypt

with open("./password-crack-dictionary.txt") as file:
	for line in file:
		word = line.strip()
		if crypt.crypt(word, "$6$bVtoNJr/GHPs7R$") == password_hash:
			print(word)
