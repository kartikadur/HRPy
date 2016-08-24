text ="ri5mfxmnsl.sjy/hwduyt"
text2 = ""
for letter in text:
	if(letter == "." or letter =="/"):
		text2 += letter		
	else :
		if letter == 'a' or letter == 'b' or letter == 'c' or letter == 'd' or letter == 'e':
			letter = chr(ord(letter) + 26) 
		text2 += chr(ord(letter) - 5)

print(text2)