from __future__ import division
import nltk, re, pprint
from urllib import urlopen
from nltk.corpus import PlaintextCorpusReader, stopwords
from HTMLParser import HTMLParser
from nltk.tokenize import *
from bs4 import BeautifulSoup
import os
#from nltk.book import *
from transcriptObject import transcriptObject
from nltk.tokenize.punkt import PunktWordTokenizer
import csv

def getCorpusFiles():
    #file names for all the documents in the corpus of transcripts
    corpus_root = ".\Transcripts"
    wordlists = PlaintextCorpusReader(corpus_root, '.*')
    fileIds = wordlists.fileids()
    return fileIds
    
def fileWriter(newpath, speakerIds, whatTheySaid): 
    #print "writing files!"
    
    if not os.path.exists(newpath): os.makedirs(newpath)         
    for index, speaker in enumerate(speakerIds):
        filePath = os.path.join(newpath,speaker +'.txt')
        
        file = open(filePath, 'a')

        for word in whatTheySaid[index]:
            file.write("%s\n" % word.encode("UTF-8"))
        file.close()  
        







corpusFiles = getCorpusFiles()                           
                                                                                    
#for each transcript in the corpus
for index, file in enumerate(corpusFiles[2016:]):
    #open specific transcript
    transcript = transcriptObject(file)
    
    #Isolates the Name of the Case from the transcript
    caseName = transcript.case_name
    
    #creates newpath for the folder/directory and creates it
    #file[:4] = The appropriate year directory
    #caseName[:149] = largest character size allowed for file names
    newpath = os.path.join(os.getcwd(),
                        'Output Documentation',
                        'byPerson',
                        transcript.case_year,
                        caseName[:100])

    speakerIds = [row['id'] for row in transcript.speaker_info]

    
    
    ########
    whatTheySaid = [[] for name in range(len(transcript.speaker_info))]
    ########
    
    for speakerSet in transcript.soup.findAll('turn'):
        w = WhitespaceTokenizer().tokenize(speakerSet.text.lower())
        whatTheySaid[speakerIds.index(speakerSet['speaker'])].extend(w)
            #[z for z in w if not w in stopwords.words('english')])


    fileWriter(newpath,speakerIds,whatTheySaid)
    
    ##monitor program progress
    #if file[:4] != corpusFiles[index - 1][:4]:
    #    print file[:4]
        

        



##transcript = open('C:\Users\Brent\Documents\My Research\Supreme Court Justices\Transcripts\\' + idsIds[1], 'rU')
##soup = BeautifulSoup(transcript)
##caseName = soup.title.text
#speakerIds = []
#speakerNames = []
#for speaker in range(len(soup.findAll("speaker"))):
#  speakerIds.append(soup.findAll("speaker")[speaker]['id'])
#  speakerNames.append(soup.findAll("speaker")[speaker].text)
#
#whatTheySaid = [[] for name in range(len(speakerNames))]
#for speakerSet in soup.findAll("turn"):
#    if (speakerSet['speaker'] in speakerIds):
#        for words in speakerSet.findAll("text"):
#            w = words.text.lower()
#            whatTheySaid[speakerIds.index(speakerSet['speaker'])].extend(WhitespaceTokenizer().tokenize(w))
#            whatTheySaid[speakerIds.index(speakerSet['speaker'])] = [w for w in whatTheySaid[speakerIds.index(speakerSet['speaker'])] if not w in stopwords.words('english')]

    

def frequencyDistribution(words):

    fhtml = FreqDist(words)
    fhtml.plot(20)


#def conditionalFreqDist():
#     cfd = nltk.ConditionalFreqDist((target, fileid) 
#     for fileid in range(StaticVariables.documentRangeEnd - StaticVariables.documentRangeBegin)
#     for word in WhitespaceTokenizer().tokenize(byTime[fileid])
#     for target in ['russia', 'soviet']
#     if word.lower().startswith(target))
#     cumTest = raw_input("Cumulative? True or False: ")
#     if cumTest == True
#     cfd.plot(cumulative = cumTest)
           