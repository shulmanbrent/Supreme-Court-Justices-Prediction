import nltk 
import os
from nltk.tokenize import WhitespaceTokenizer, wordpunct_tokenize
from transcriptObject import transcriptObject
import utilities

def main():
    #boolean options
    remove_punct = utilities.remove_punct_option()
    remove_common_words = utilities.remove_common_words_option()
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    #for each transcript in the corpus
    for index, file in enumerate(utilities.get_corpus_files()):
        #open specific transcript as object
        transcript = transcriptObject(file)

        #creates newpath for the folder/directory and creates it
        #caseName[:100] = helps limit file name size
        newpath = os.path.join(os.getcwd(),
                            'Output Documentation',
                            'byPerson',
                            transcript.case_year,
                            utilities.get_folder_name((transcript.case_name)[:100]))
                            #handles name length error ^^^
                            
        speakerIds = [row['id'] for row in transcript.speaker_info]
    
    
        #2-d array of variable length depending on number of speakers
        whatTheySaid = [[] for name in range(len(transcript.speaker_info))]
    
        #each 'turn' corresponds to one person speaking
        #the next 'turn' is when another person begins speaking
        for speakerSet in transcript.soup.findAll('turn'):
            w = []
            if remove_punct:
                w = nltk.wordpunct_tokenize(speakerSet.text.lower())
                w = utilities.remove_punctuation(w)
            elif remove_punct == False:        
                w = WhitespaceTokenizer().tokenize(speakerSet.text.lower())
            
            if remove_common_words:
                w = utilities.remove_common_words()
            
            #at the index corresponding to the speaker -> add what they said
            whatTheySaid[speakerIds.index(speakerSet['speaker'])].extend(w)
                
    
    
        if not os.path.exists(newpath): os.makedirs(newpath)         
        for index, speaker in enumerate(speakerIds):
            filePath = os.path.join(newpath,speaker +'.txt')
            
            file = open(filePath, 'a')
    
            for word in whatTheySaid[index]:
                file.write("%s\n" % word.encode("UTF-8"))
            file.close()

if __name__ == "__main__":
    main()