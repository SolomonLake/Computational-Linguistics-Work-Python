import nltk
from nltk.corpus import brown
from text import *

"""
Step 1:
state - 
around - 
"""

def MostLikelyTag (word):
	wordTagCount = {}
	for wordTagList in brown.tagged_words():
		if (wordTagList[0] == word):
			if (wordTagList[1] in wordTagCount):
				wordTagCount[wordTagList[1]] += 1
			else:
				wordTagCount[wordTagList[1]] = 0

	if (len(wordTagCount.keys()) == 0):
		return "NN"
	mLT = next (iter (wordTagCount.values()))
	for tag in wordTagCount:
		if (wordTagCount[tag] > wordTagCount[mLT]):
			mLT = wordTagCount[tag]
	return mLT

# used http://stackoverflow.com/questions/3097866/access-an-arbitrary-element-in-a-dictionary-in-python
# 	to get arbitrary-element-in-a-dictionary-in-python


"""
Step 2:
"""

def ApplyMLTag (text):
	wordMLTagDict = {}
	returnList = []
	for word in text:
		if (word not in wordMLTagDict):
			wordMLTagDict[word] = MostLikelyTag (word)
		returnList.append((word, wordMLTagDict[word]))
	return returnList

# separates periods, commas, and n't
def ParseText (text):
	returnText = []
	for i in range (0, len(text)):
		if (text[i].endswith('.') or text[i].endswith(',') or text[i].endswith('n\'t')):
			returnText.append(text[i][:-1])
			returnText.append(text[i][-1:])
		else:
			returnText.append(text[i])
	return returnTest


# help with checking if dictionary is empty: http://stackoverflow.com/questions/13312043/pythonefficient-way-to-check-if-dictionary-is-empty-or-not









