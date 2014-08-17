from __future__ import division
from nltk.corpus import PlaintextCorpusReader

#file names for all the documents in the corpus of transcripts
corpus_root = 'C:\Users\Brent\Documents\My Research\Supreme Court Justices\Transcripts'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
#array of all the fileIds
fileIds = wordlists.fileids()

def speakers():
    #array that will contain all the Names of speakers in a court case document
    global allNames
    allNames = []
    
    #opens file to be written containing all the names
    file = open("allNames.txt", 'w')
    
    
    for i in fileIds:
        #opens tracript at fileId --> i
        speakerNames = open('C:\Users\Brent\Documents\My Research\Supreme Court Justices\Transcripts\\' + i, 'rU')
        speakerNames = speakerNames.read()
        #deletes unecessary text
        speakerNames = speakerNames.split('<speaker ', 1)[1]
        speakerNames = speakerNames.split('id="')
        
        #Splits text at each new speaker id
        for j in range(len(speakerNames)):
            speakerNames[j] = speakerNames[j].split('" type=')[0]
        #gets rid of unnecessary first list item
        speakerNames.pop(0)
        
        #appends list of names to allNames array
        allNames.append(speakerNames)
    
    #writes the file allNames
    if (raw_input("Would you like to create a file (Y/N): ") == 'Y'):
        for i in range(len(allNames)):
            for j in allNames[i]:
                file.write(j + " ")
            file.write("\n")
        file.close()
    
def titles():
    #array that will contain all the Titles of all the court cases 
    global allTitles
    allTitles = []

    #opens file to be written containing all the names
    file = open("allTitles.txt", 'w')
    
    
    for i in fileIds:
        #Opens transcript at fileId --> i
        caseNames = open('C:\Users\Brent\Documents\My Research\Supreme Court Justices\Transcripts\\' + i, 'rU')
        caseNames = caseNames.read()
        
        #edge-case that file contains no title
        if ('title/' in caseNames): 
            caseNames = "No Title"
        else:
            #strips out just the title from the xml
            caseNames = caseNames.split('<title>', 1)[1]
            caseNames = caseNames.split('</title>', 1)[0]
               
        #appends list of case names to allTitles array
        allTitles.append(caseNames)
     
    if (raw_input('Would you like to create a file (Y/N):') == 'Y'):  
        for i in allTitles:    
            file.write(i + "\n")
        file.close()


    
#main:
speakers() #output --> global allNames [[]] with all speakers ids in each case 
titles() #output --> global allTitles [] with all the case titles in order