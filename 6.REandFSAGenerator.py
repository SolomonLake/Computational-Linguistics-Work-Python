# Name: Solomon Lake Giffen-Hunter

import nltk, re
from nltk.corpus import gutenberg



class FSA:
  def __init__(self, alpha, states, start, finals, transitions):
    self.Sigma = alpha       #set of allowed symbols
    self.Q = states          #set of qs
    self.q0 = start          #string = q0
    self.F = finals          #set of qs
    self.delta = transitions #dict mapping qs to dicts mapping symbols to the dest q

  def recognize(self,string):
    curQ = self.q0
    for sym in string:
      if (sym not in self.Sigma):
        return False
      if (sym not in self.delta[curQ]):
        return False
      curQ = self.delta[curQ][sym]
        
    if (curQ in self.F):
      return True
    return False

######### Part 1 ##########

def RE_example():
   myre = re.compile('Mr\.\s[A-z]+')
   mytext = gutenberg.raw('austen-emma.txt')
   tokens = myre.findall(mytext)
   print 'Found',len(tokens),'matches.'

ceasar = nltk.corpus.gutenberg.fileids()[14] #shakespeare-ceasar
# All strings that are sentences that contain the word "Sword" and capitalized words that start with V
def my_RE_example():
  myre = re.compile('\n.*Sword.*\n')
  mytext = gutenberg.raw(ceasar)
  tokens = myre.findall(mytext)
  print 'Found',len(tokens),'sentences with the word Sword.'
  
  # Second example:
  myre = re.compile('[V][a-z]+')
  mytext = gutenberg.raw(ceasar)
  tokens = myre.findall(mytext)
  print 'Found',len(tokens),'capitalized words that begin with \'V\''

######### Part 2 ##########

# Create an FSA that recognizes the following language: strings of a's and b's such that the string 1) starts with 'a', 2) ends with 'b', and 3) has an even number of a's.

#Help with set syntax: https://www.dotnetperls.com/set-python
myFSA = FSA({'a','b'}, {'q0','q1','q2','q3'}, 'q0', {'q3'}, {'q0':{'a':'q1'}, 'q1':{'a':'q2', 'b':'q1'}, 'q2':{'a':'q1', 'b':'q3'}, 'q3':{'a':'q1', 'b':'q3'}})

def FSA_test(myFSA):
    print 'The following tests should all return True:'
    print 'aab',myFSA.recognize('aab')
    print 'aabaab',myFSA.recognize('aabaab')
    print 'abaaababab',myFSA.recognize('abaaababab')

    print 'The following tests should all return False:'
    print 'baab',myFSA.recognize('baab')
    print 'aaaa',myFSA.recognize('aaaa')
    print 'aaab',myFSA.recognize('aaab')
    print 'aabbaaab',myFSA.recognize('aabbaaab')
    


my_RE_example()
FSA_test(myFSA)

    
