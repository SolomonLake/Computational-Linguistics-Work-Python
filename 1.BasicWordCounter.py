import nltk
from nltk.corpus import inaugural



def WordCounter (myString):
	print ("string is: " + myString)
	for file in inaugural.fileids():
		count = 0
		for word in inaugural.words(file):
			if (word == myString):
				count += 1
				#print (word)
		print (file[0:4] + " " + str(count))


# used https://docs.python.org/2/library/string.html for string index operations
# used https://www.techwalla.com/articles/how-to-convert-int-to-string-in-python for int to string conversion




WordCounter("God")