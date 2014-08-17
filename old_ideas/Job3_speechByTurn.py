from __future__ import division
import nltk
from nltk.corpus import PlaintextCorpusReader
import os

#file names for all the documents in the corpus of transcripts
corpus_root = 'C:\Users\Brent\Documents\My Research\Supreme Court Justices\Transcripts'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
fileIds = wordlists.fileids()

global speechByTurn

speechByTurn = [[] for i in range(len(fileIds))]


def byTurn():
    
    #opens file allDataByTurn.txt to be written
    
    
    #reads in txt of all speakers of each case by line
    speakerNames = open('C:\Users\Brent\Documents\My Research\Supreme Court Justices\\allNames.txt', 'rU')
    speakerNames = speakerNames.read()
    speakerNames = speakerNames.splitlines()
    
    #splits up names into a 2-d array
    for i in range(len(speakerNames)):
        speakerNames[i] = speakerNames[i].split()
    
    #reads in txt of all the names of each case
    caseNames = open('C:\Users\Brent\Documents\My Research\Supreme Court Justices\\allTitles.txt', 'rU')
    caseNames = caseNames.read()
    caseNames = caseNames.splitlines()
    
    
    for i in range(len(fileIds)):
        path = 'C:\Users\Brent\Documents\My Research\Supreme Court Justices\Output Documentation\\' + fileIds[i][:4]
        completeName = os.path.join(path, fileIds[i][:4] + " " + caseNames[i].replace('"', '').replace('/', ' ')[:30] + '.txt')         
        
        file = open(completeName, 'w')
        file.write(caseNames[i] + '\n')
        
        transcript = open('C:\Users\Brent\Documents\My Research\Supreme Court Justices\Transcripts\\' + fileIds[i], 'rU')
        transcript = transcript.read()
        transcript = transcript.split('</resources>', 1)[1]
        transcript = transcript.split('<turn ')
        for j in range(len(transcript)):
            for nameId in speakerNames[i]:
                if nameId in transcript[j]:
                    transcript[j] = nltk.clean_html(transcript[j])
                    #transcript[j] = transcript[j].split('>', 1)[1]
                    speechByTurn[i].append(transcript[j])
                    
                    file.write(transcript[j] + '\n')
        
        file.close() 
                         
#main:
byTurn()