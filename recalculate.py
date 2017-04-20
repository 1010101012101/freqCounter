#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:40:46 2017

@author: yjiang
"""

import gensim, logging, nltk, re, os, sys
from nltk.stem.snowball import SnowballStemmer
from gensim.models import Phrases

stopwords = nltk.corpus.stopwords.words('english')
stemmer = SnowballStemmer("english")

bigram = Phrases.load('model/bigram')
trigram = Phrases.load('model/trigram')

def tokenize_stem_stop(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for word in nltk.word_tokenize(text) if word not in stopwords]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z0-9]', token):
            filtered_tokens.append(token)
    #stems = [stemmer.stem(t) for t in tokens]
    return filtered_tokens

def recal(path):
    result = {}
    for line in open(path):
        text = tokenize_stem_stop(line.rsplit(' ', 1)[0].lower())
        parsed_text = trigram[bigram[text]]
        value = int(line.rsplit(' ', 1)[1])
        for term in parsed_text:
            w = 1
            if not term.isdigit() and len(term)>2:
                if len(text)>4 and '_' in term:
                   w = 50
                if term in result:
                   result[term] = result[term] + value*w
                else:
                   result[term] = value*w
    return result

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

output = recal('/Users/yjiang/Documents/pythonWorkspace/freqCounter/data/agg_self_200.txt')
sorted_output = sorted(output.items(), key=lambda x: x[1], reverse=True)
with open("output/output_self_200.csv", "w") as text_file:
    for out in sorted_output:
        if not hasNumbers(out[0]) and out[1]>=50:
               text_file.write("{0},{1}\n".format(out[0], out[1]))

# sent = ['near', 'earth', 'object', 'planetary', 'society']
# print(trigram[bigram[sent]])