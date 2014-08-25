import csv
import nltk
import utilities
from transcriptObject import transcriptObject

with open('SCDB_2013_01_justiceCentered_Citation.csv', 'r') as csvfile:
    read = csv.reader(csvfile)
    titles = []
    global info
    info = [] 
    for index, row in enumerate(read):
        if index == 0:
            titles = row
        else:
            w = dict(zip(titles,row))
            if int(w['caseId'][:4]) >= 1955:
                info.append(w)

#for index, file in enumerate(utilities.get_corpus_files()[:1000]):
#    #open specific transcript as object
#    transcript = transcriptObject(file)
#    for index2, line in enumerate(info):
#        temp1 = nltk.wordpunct_tokenize(line['caseName'].lower())
#        temp1 = ' '.join(utilities.remove_punctuation(temp1))
#        if transcript.case_year == int(line['caseId'][:4]):
#           if transcript.case_name.lower() == temp1:
#               print "Hooray"
matches = 0
total = 0
for index, file in enumerate(utilities.get_corpus_files()[1000]):
    #open specific transcript as object
    transcript = transcriptObject(file)
    for case in info:
        #if case['dateArgument'][-4:] == transcript.date_of_arg['year']:
        if case['docket'] == transcript.docket_number:
            matches += 1

#plane ideas
#match docetnumbers to see if case has match
#find possible inconsistensies between the data
#
