from __future__ import division
from nltk.corpus import PlaintextCorpusReader
import os

corpus_root = 'C:\Users\Brent\Documents\My Research\Supreme Court Justices\Output Documentation\speechByTurn'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
fileIds = wordlists.fileids()

global speechByPerson

speechByPerson = []

def byPerson():
    
    #reads in txt of all speakers of each case by line
    speakerNames = open('C:\Users\Brent\Documents\My Research\Supreme Court Justices\\allNames.txt', 'rU')
    speakerNames = speakerNames.read()
    speakerNames = speakerNames.splitlines()
    
    #splits up names into a 2-d array
    for i in range(len(speakerNames)):
        speakerNames[i] = speakerNames[i].split()
   
    caseNames = open('C:\Users\Brent\Documents\My Research\Supreme Court Justices\\allTitles.txt', 'rU')
    caseNames = caseNames.read()
    caseNames = caseNames.splitlines()
    
    for i in range(len(fileIds)):
        x = [''] * len(speakerNames[i])
        speechByPerson.append(x)
     
    for i in range(len(fileIds)):
        
        transcript = open('C:\Users\Brent\Documents\My Research\Supreme Court Justices\Output Documentation\speechByTurn\\' + fileIds[i], 'rU')
        transcript = transcript.read()
        transcript = transcript.split('speaker=')

        for j in range(len(transcript)):
            for nameId in speakerNames[i]:
                if nameId in transcript[j]:
                    personIndex = speakerNames[i].index(nameId)
                    transcript[j] = transcript[j].split('>', 1)[1]
                    speechByPerson[i][personIndex] += transcript[j]
                    break
    if raw_input("Would you like to write the files? ") == "Yes":
        writeFile(caseNames)
 
def writeFile(caseNames): 
    for i in range(len(fileIds)):
        path = 'C:\Users\Brent\Documents\My Research\Supreme Court Justices\Output Documentation\speechByPerson\\' + fileIds[i][:4]
        completeName = os.path.join(path, caseNames[i].replace('"', '').replace('/', ' ')[:30] + '.txt')
    
        file = open(completeName, 'w')
        for j in range(len(speechByPerson[i])):
            file.write(speechByPerson[i][j])                 
                        
        
        
        file.close() 
 
#main:
byPerson()


        
    
    
    
    