import nltk
from nltk.corpus import treebank
from nltk.tree import Tree

#Lake Giffen-Hunter

"""
Sources:
List operations: http://www.thegeekstuff.com/2013/06/python-list/?utm_source=feedly
All tree operations: http://www.nltk.org/api/nltk.html#module-nltk.tree
"""

#print treebank.fileids()

mySen = treebank.parsed_sents(u'wsj_0002.mrg')[0]

#print mySen.leaves()

EngToSpaDict = {"years": "anos", "old": "viejo", "and": "y", "former": "anterior", "chairman": "presidente", "of": "de", "was": "estaba", "named": "llamado", "a": "un", "nonexecutive": "no ejecutivo", "director": "director", "this": "esta", "British": "britanico", "industrial": "industrial", "conglomerate": "conglomerado"}       


def NP__ADJ_NNtoNP__NN_ADJ(t):
    if (t.label() == "NP"):
        JJs = []
        NNtoSwitch = None
        for child in t:
            if (child.label() == "JJ" and t.index(child) != len(t)-1):
                #last condition is to prevent phrases ending in JJs from error
                JJs.append(child)
            elif (child.label() == "NN" and len(JJs) != 0):
                NNtoSwitch = child
                break
            elif (len(JJs) != 0):
                #case where we had some Adjs but found a non-Adj/NN
                JJs = []
                
        if (len(JJs) != 0):
            for j in JJs:
                t.remove(j)
            i = t.index(NNtoSwitch)
            for j in JJs:
                t.insert(i+1, j)
            
    for child in t:
        if (len(child) > 1):
            NP__ADJ_NNtoNP__NN_ADJ(child)
    if (t.label() == "S"):
        return t

print mySen
print "\n"
print "After NP -> ADJ NN to NP -> NN ADJ has been applied"
print NP__ADJ_NNtoNP__NN_ADJ(mySen)
print "\n"

print "Translated to Spanish:"
for pos in mySen.treepositions('leaves'):
    if (mySen[pos] in EngToSpaDict):
        mySen[pos] = EngToSpaDict[mySen[pos]]

print mySen







"""
Testing purposes

#mySen.set_label("F")
#mySen[0] = Tree("NN", ["hello"])

#mySen.append(Tree("NP", [Tree("Hey", ["1"]), Tree("JJ", ["Adjj"])]))

#print mySen

for s in mySen.subtrees(lambda mySen: mySen.label() == "NP"):
    if (s[0].label() == "NN"):
        if (len(s) > 1):
            if (s[1].label() == "NNS"):
                print s

def findSentence():
    for f in treebank.fileids():
        for s in treebank.parsed_sents(f):
            for t in s.subtrees(lambda s: s.label() == "NP"):
                if (t[0].label() == "JJ"):
                    if (len(t) > 1):
                        if (t[1].label() == "NN"):
                            return f
                            
#print findSentence()
"""

