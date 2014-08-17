from __future__ import division

def printTitleAndSpeakers():
    #opens file to be written
    file = open("TitlesAndSpeakers.txt", 'w')
    
    #opens allTitles file and separetes it into an array
    caseNames = open('C:\Users\Brent\Documents\My Research\Supreme Court Justices\\allTitles.txt', 'rU')
    caseNames = caseNames.read()
    caseNames = caseNames.splitlines()
    
    #opens allNames file and separates it into anrray by case
    speakerNames = open('C:\Users\Brent\Documents\My Research\Supreme Court Justices\\allNames.txt', 'rU')
    speakerNames = speakerNames.read()
    speakerNames = speakerNames.splitlines()
    
    #writse file to contain both caseName and speackerNames
    for i in range(len(speakerNames)):
         file.write(caseNames[i] + ": " + speakerNames[i] + '\n')
    file.close()
    


printTitleAndSpeakers()