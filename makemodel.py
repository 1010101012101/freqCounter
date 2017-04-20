#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:29:38 2017

@author: yjiang
"""

import gensim, logging, nltk, re, os, sys
from nltk.stem.snowball import SnowballStemmer
from gensim.models import Phrases

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#==============================================================================
reload(sys)
sys.setdefaultencoding('utf-8')
#==============================================================================

stopwords = nltk.corpus.stopwords.words('english')
stemmer = SnowballStemmer("english")

def tokenize_stem_stop(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for word in nltk.word_tokenize(text) if word not in stopwords]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z0-9]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in tokens]
    return stems

def makesent(path):
    result = []
    for line in open(path):
        result.append(tokenize_stem_stop(line.rsplit(' ', 1)[0].lower()))
    return result

sentences = makesent('/Users/yjiang/Documents/pythonWorkspace/freqCounter/data/agg_self_in_200.txt')
print(sentences)
bigram = Phrases(sentences, min_count=1, threshold=1)
bi_sent = bigram[sentences]
trigram = Phrases(bigram[sentences], min_count=1, threshold=1)

#==============================================================================
# for phrase, score in trigram.export_phrases(bi_sent):
#     print(u'{0}   {1}'.format(phrase, score))
#==============================================================================

bigram.save('model/bigram')
trigram.save('model/trigram')
