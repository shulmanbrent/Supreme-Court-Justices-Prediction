from __future__ import division
import nltk
from nltk.corpus import PlaintextCorpusReader
from bs4 import BeautifulSoup
import os

def getTranscriptIds():
    #file names for all the documents in the corpus of transcripts
    corpus_root = ".\Transcripts"
    wordlists = PlaintextCorpusReader(corpus_root, '.*')
    return wordlists.fileids()

def getCaseName(transcript):
    return transcript.title.text



def create_FolderByCase():

    fileIds = getTranscriptIds()
    
    #for each transcript in the corpus
    for ids in fileIds:
    
        #open specific transcript
        transcript = open(os.path.join(os.getcwd(), 'Transcripts', ids), 'r')
        
        #allows for use of BeautifulSoup API
        transcript = BeautifulSoup(transcript)
        
        #Isolates the Name of the Case from the transcript
        caseName = removeBadCharacters(getCaseName(transcript))
        
        #creates newpath for the folder/directory and creates it
        #ids[:4] = The appropriate year directory
        newpath = os.path.join(os.getcwd(),'Output Documentation', 'byPersonCSV', ids[:4], caseName[:148])
        if not os.path.exists(newpath): os.makedirs(newpath)


        monitorProgress(ids, fileIds)
        
def monitorProgress(ids, fileIds):
    def ask():
        if fileIds.index(ids) == 0: 
            monitor = raw_input("Would you like to use print statements to monitor the program progress? (Y/N) ") 
            while (not (monitor == "Y" or monitor == "N")):
                monitor = raw_input("ERROR - Invalid input: Would you like to monitor the program progress? (Y/N) ")
            if monitor == "N": return False
        return True
        
    if ask() == True and ids [:4] != fileIds[fileIds.index(ids) - 1][:4]:
            print ids[:4]
    return


