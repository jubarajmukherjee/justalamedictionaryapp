import json		#json library imported
from difflib import get_close_matches


data = json.load(open("data.json")) #the info stored in the json loaded to data for use in program

def translate(word):
	word = word.lower() 	#converted to lowercase to remove case-sensitive error
	if word in data:		#when word is present it's true, so checks for presence of word 
		return data[word]	
	elif len(get_close_matches(word,data.keys(),n=1,cutoff=0.8))>0:	#checks if there are any close matches to the word
		yn = input("Did you mean %s? Press Y for Yes and N for No: " % get_close_matches(word,data.keys(),n=3,cutoff=0.8)[0])
		yn = yn.lower() #converts input to lowercase to avoid case sentivity issues/errors
		if yn =="y":
			return data[get_close_matches(word,data.keys(),n=3,cutoff=0.8)[0]] #returns the closest match to the word
		elif yn =="n":
			return "The word is not available in the dictionary"
		else:
			return "Didn't get that mate."	
	else:
		return "The word is not available in this dictionary."



word=input("Enter the word: ")	#user input

output = translate(word)

if type(output) == list: #checks if the definition is returned from json as a list
	for item in output:
		print(item) # helps to print the definition from json file one by one instead of a list, making it more readable
else:
	print(output)	# prints all the other cases


