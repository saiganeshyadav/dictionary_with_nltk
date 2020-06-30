import nltk
from nltk.corpus import wordnet
word=input("enter word:")
synonyms=[]
antonyms=[]
definitions=[]
examples=[]
for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

for syn in wordnet.synsets(word):
    for l in syn.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

for dfn in wordnet.synsets(word):
    definitions.append(dfn.definition())

for ex in wordnet.synsets(word):
    if ex.examples():
        examples.append(ex.examples()[0])
print('definitions:')
try:
    for i in range(2):
        print(definitions[i])
except:
    print("sorry")
print('examples:')
try:
    for i in range(2):
        print(examples[i])
except:
    print("sorry")
print("synonyms:")
try:
    for i in range(2):
        print(synonyms[i])
except:
    print("sorry")
print("antonyms:")
try:
    for i in range(2):
        print(antonyms[i])
except:
    print("sorry")
    

    
