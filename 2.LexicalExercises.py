import nltk
from nltk.book import*

"""
Lexical diversity definition clarification:
http://journals.lub.lu.se/index.php/LWPL/article/download/2273/1848

It seems like the language of the Inaugural Address is much more diverse, with 9754
different words, compared to Monty Python Holy Grail which just has 2166. Sense and
Sensibility is somewhere in the middle.

"""
def LexicalDiversityDict (wordList):
    print (wordList)
    foundWords = {}
    for word in wordList:
        if (word not in foundWords):
            foundWords[word] = 1
        else:
            foundWords[word] = foundWords[word] + 1
    return foundWords

def LexicalDiversity (wordList):
    words = LexicalDiversityDict(wordList)
    return len(words)
        
# used this: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# for help with dictionaries

"""
A much lower percentage of the words in Monty Python and Sense and Sensibility are 'the'.
The Inaugural Address had over 6 percent, wheras the other two had less than 3. This could be due
to the formality of the Inaugural Addresses?
"""

def PercentageUse (word, words):
    wordsDict = LexicalDiversityDict(words)
    wordCount = wordsDict[word]
    return (float(wordCount*100)) / float(len(words))


"""
There are 14484 words that begin with "un".

I hypothesize that there are more 'th' starts to words than 'ch' starts.
'th': 1799
'ch': 2527
"""

def FindBegin (beginStr):
    print (beginStr)
    wordList = nltk.corpus.words.words('en')
    returnList = []
    for word in wordList:
        if (word[0:len(beginStr)] == beginStr):
            returnList.insert(0,word)
    return len(returnList)


print(LexicalDiversity (text2))
print(LexicalDiversity (text4))
print(LexicalDiversity (text6))


print PercentageUse ("the", text2)
print PercentageUse ("the", text4)
print PercentageUse ("the", text6)


print (FindBegin("un"))


