from __future__ import division
import nltk, re, pprint
from urllib import urlopen
from nltk.corpus import PlaintextCorpusReader, stopwords
from HTMLParser import HTMLParser
from nltk.tokenize import *
import shutil, os
from bs4 import BeautifulSoup

    
corpus_root = 'C:\Users\Brent\Documents\My Research\Supreme Court Justices\Output Documentation\\1959\\yo\\'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
fileIds = wordlists.fileids()

for i in range(1959, 2014):
    for name in fileIds:
        print name
        if str(i) in name:
            os.rename('C:\Users\Brent\Documents\My Research\Supreme Court Justices\Output Documentation\\1959\\yo\\' + name, 'C:\Users\Brent\Documents\My Research\Supreme Court Justices\Output Documentation\\1959')
        