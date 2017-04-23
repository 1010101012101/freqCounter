#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 11:57:04 2017

@author: yjiang
"""
import gensim, logging, nltk, re, os, sys
from nltk.stem import PorterStemmer

stemmer=PorterStemmer()

def convertEva(path):
    result = {}
    for line in open(path):
        text = line.split(',')
        result[text[0]] = text[1]          
    return result

def stemstring(phrase):
    stems = [stemmer.stem(w) for w in phrase.split(" ")]
    return " ".join(stems)

output = convertEva('/Users/yjiang/Documents/nutch_data/keyword_evaluation/output_self_in_200_cleanup.csv')
sorted_output = sorted(output.items(), key=lambda x: x[1], reverse=True)
with open("/Users/yjiang/Documents/nutch_data/keyword_evaluation/evaluation_formatted.txt", "w") as text_file:
    for out in sorted_output:
        if int(out[1])>1:
               text_file.write("{0},{1}".format(stemstring(out[0].replace('_', ' ')), out[1]))
#print(stemmer.stem('mitigation'))