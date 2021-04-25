import json		#json library imported
from difflib import get_close_matches


data = json.load(open("data.json")) #the info stored in the json loaded to data for use in program

def translate(word):
	word = word.lower() 	#converted to lowercase to remove case-sensitive error
	if word in data:		#when word is present it's true, so checks for presence of word 
		return data[word]	
	elif len(get_close_matches(word,data.keys(),n=1,cutoff=0.8))>0:
		yn = input("Did you mean %s? Press Y for Yes and N for No: " % get_close_matches(word,data.keys(),n=3,cutoff=0.8)[0])
		yn = yn.lower()
		if yn =="y":
			return data[get_close_matches(word,data.keys(),n=3,cutoff=0.8)[0]] 
		elif yn =="n":
			return "The word is not available in the dictionary"
		else:
			return "Didn't get that mate."	
	else:
		return "The word is not available in this dictionary."



word=input("Enter the word: ")		#user input

output = translate(word)

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)		


