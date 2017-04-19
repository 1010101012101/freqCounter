#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:40:46 2017

@author: yjiang
"""

import gensim, logging, nltk, re, os, sys
from nltk.stem.lancaster import LancasterStemmer
from gensim.models import Phrases

bigram = Phrases.load('model/bigram')
trigram = Phrases.load('model/trigram')
sent = ['near', 'earth', 'object']

print(trigram[bigram[sent]])