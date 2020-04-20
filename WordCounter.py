import re

''' ########################################

		The code Below reads in the input file and
		stores the results into one large string
		
    #########################################'''
with open('input.txt', 'r') as myfile:
    block = myfile.read()

''' #########################################
		
		The string is then rearanged into a format that can be 
		esily manipulated
	
    ##########################################'''
badChars = ['\'', '\\', '`', '~', '(', ')', '[', '.', ',', '!', '?', '"', '"', '-', '1', '2', '3', '4', '5', '6', '7',
            '8', '9', '0', ']', '“', '”', '|', '+', '=', '@', ':', '<', '>', '#', '$', '%', '^', '&', '*', ';', '_', '/']
for i in badChars:
    block = block.replace(i, '')

block = block.lower()

document = block.split()

''' #########################################

		The string is then broken up into a dictionary of words and 
		their occurances.

		then the results of the dictionary are placed in an
		array where it is then sorted by number of occurances
		then outputed into a file.

    ##########################################'''

dict = {}
totalWords = 0

for word in document:
    dict[word] = dict.get(word, 0) + 1
    totalWords += 1

wordCount = []

for txt, num in dict.items():
    wordCount.append((num, txt))

wordCount.sort(reverse=True)

''' ######################################
		
		File output occurs here
		*now with frequency of top words!*

    ######################################'''
#print("\n".join('%s %s' % x for x in wordCount[0:5]))


ofile = open('output.txt', 'w+')
ofile.write("Top 5 most common words in File: \n")
for num,txt in wordCount[0:5]:
    freq = num / totalWords
    freq *= 100
    ofile.write(str(txt))
    ofile.write(" ")
    ofile.write(str(round(freq,2)))
    ofile.write(" ")
    ofile.write('% \n')
ofile.write('\n')
ofile.write('\n'.join('%s %s' % x for x in wordCount))
ofile.close()
