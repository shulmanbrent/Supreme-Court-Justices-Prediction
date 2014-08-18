from nltk.corpus import PlaintextCorpusReader, stopwords
import nltk 
import string         

def get_corpus_files():
    #file names for all the documents in the corpus of transcripts
    corpus_root = ".\Transcripts"
    wordlists = PlaintextCorpusReader(corpus_root, '.*')
    fileIds = wordlists.fileids()
    return fileIds

   
#this is used the handle the name length error when creating files
def get_folder_name(caseName):
    #splits caseName at punctuation
    caseName = nltk.wordpunct_tokenize(caseName)
    
    #takes out punctuation if it is in badTokens and rejoins string
    caseName = remove_punctuation(caseName)
    return '-'.join(caseName)
    

def remove_punct_option():
    while True:
        user_input = raw_input("Would you like to remove punctuation? (Y/N) ")
        if user_input in ['Y', 'N']:
            break
        else:
            print('That is not a valid option!')
    
    if user_input == "Y":
        print "This might take a while..."
        return True
    else:
        return False

def remove_common_words_option():
    while True:
        user_input = raw_input("Would you like to remove common words?\neg: is, the, a,  (Y/N) ")
        if user_input in ['Y', 'N']:
            break
        else:
            print('That is not a valid option!')
    
    if user_input == "Y":
        print "This might take a while..."
        return True
    else:
        return False

#@input = tokenized array of words & punctuation
#@return = tokenized arry of words
def remove_punctuation(w):
    w = [token for token in w if token not in set(string.punctuation)]
    return w   

#@input = tokenized array of words
#@return = tokenized arry of words w/o common words
def remove_common_words(w):
    w = [token for token in w if token not in stopwords.words('english')]
    return w