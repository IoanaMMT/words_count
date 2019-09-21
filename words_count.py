'''I need you to make a function named word_count. It should accept a single argument 
which will be a string. The function needs to return a dictionary. The keys in the 
dictionary will be each of the words in the string, lowercased. The values will be how 
many times that particular word appears in the string.
Check the comments below for an example.'''

def word_count(string):
	words = string.lower().split()
	dictionary = {}
	for word in words:
		dictionary[word] = words.count(word)
		return dictionary

print(word_count("To be or not to be"))

#The expected result should be:
#{'to': 2, 'be': 2, 'or': 1, 'not': 1}
# but what I get is only : 'to': 2