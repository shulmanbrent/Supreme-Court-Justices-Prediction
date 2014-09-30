import csv
import nltk
import utilities
from transcriptObject import transcriptObject

#years start at 6583
#for index, file in enumerate(utilities.get_corpus_files()[6583:]):
#    #open specific transcript as object
#    transcript = transcriptObject(file)
#    for speaker in transcript.speaker_info:
#        if "anthony_m_kennedy" in speaker['id']:
           


    

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

def justice_filter (justiceId):
    justice_info = []
    for line in info:
        if line['justiceName'] == justiceId:
            justice_info.append(line)
    return justice_info
        

for index, file in enumerate(utilities.get_corpus_files()[6583:]):
    #open specific transcript as object
    transcript = transcriptObject(file)
    for index2, line in enumerate(justice_filter("anthony_m_kennedy")):
        if line['justiceName'] in transcript.speaker_ids:
            print line['docket']
            print transcript.case_name
            print line['caseName']
                


   

#for index, file in enumerate(utilities.get_corpus_files()):
#    #open specific transcript as object
#    transcript = transcriptObject(file)
#    for case in info:
#        if case['caseId'][:4] == transcript.date_of_arg['year']:
#            if case['docket'] == transcript.docket_number:
#                matches += 1
#                print matches
        
#plane ideas
#match docetnumbers to see if case has match
#find possible inconsistensies between the data
#
