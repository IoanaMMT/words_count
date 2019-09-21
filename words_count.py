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



"""
the following implementation is an optimization of the code above.
the above code makes use of words.count which is an internal loop on all the list's elements
that makes the count slow.

in the second implementation, I am taking the advantage of the fact that I am already going througth the list once and
counting the elements when they appear. When I first find a word I create an entry in the dictionary initializing it with 1, 
later if they are found again I just need to increment the word count by 1.
"""
def word_count2(string):
	words = string.lower().split()
	dictionary = {}
	for word in words:
		if word in dictionary:
			dictionary[word] += 1
		else:
			dictionary[word] = 1

	return dictionary

print(word_count2("To be or not to be"))