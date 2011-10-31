#!/usr/bin/env python

import sys

network = []
word = ""
filename = ""

# 1. Accept the input word
# Some sanity checking
if ( len(sys.argv) > 1):
	word 		= sys.argv[1]
	filename 	= sys.argv[2] 

else:
	print "network script is run using network.py [word] [file_to_search] \n"
	exit()

print " Starting to search for the networks of : " + word + "\n"


#2. How are we going to find all the words that have a Levenshtein distance of 1?
#	- 1. We could search through all words and see by what distance they differ from the input word
#		ie: take causes and challenge, we could examine how much of the word matches, if they 
#		contain a minimum number of letters then let's see what the distance is
#		let's give this a first pass and see how it goes.

# Some initilization

word_length = len(word)

file = open(filename, 'r')  
for line in file:
	test_word = line.strip()
	test_word_length = len(test_word)
	# First check the size to rule out any weird possibilities
	if ( ( word_length > (test_word_length + 1) ) or ( test_word_length > (word_length + 1))):
		# Not a match since they differ by more then 1 in length
		print " Words differ by more then 2: " , test_word
	# Here the lengths are close so we need to check if we can make a 
	#match by doign the following: 1. add a letter 2. subtract a letter 3. change a letter
	if( word_length < test_word_length):

		# Since the test_word is longer, let's add the first or laster letter
		first_add_word = test_word[0] + word
		last_add_word = word + test_word[test_word_length - 1]
		
		# Did adding the first letter of the longer test work? 
		if( first_add_word == test_word):
			print "appending first: " , first_add_word , test_word
			network.append(test_word)			
		# Did adding the last letter of the longer work?
		elif( last_add_word == test_word):
			print "appending last: " , last_add_word , test_word
			network.append(test_word)			
	
	elif( word_length > test_word_length):	
		# Since the test_word is longer, let's add the first or laster letter
		first_add_word = test_word[0] + word
		last_add_word  = test_word + test_word[test_word_length - 1]
		
		# Did adding the first letter of the longer test work? 
		if( first_add_word == test_word):
			print "appending first: " , first_add_word , test_word
			network.append(test_word)			
		
		elif( last_add_word == test_word):
			print "appending last: " , last_add_word , test_word
			network.append(test_word)			
			
		# Did adding the last letter of the longer work?

	elif( word_length == test_word_length):
		# Let's try changing some of the letters to see if we can find a match
		# Change the letters of the two words to see if we can find a match
		for i in range(0, word_length):
			if ( word[i] != test_word[i]):
				test = list(word)
				del(test[i])
				test.insert(i,test_word[i])
				
				if( test == list(test_word)):
					network.append(test_word)


print network
