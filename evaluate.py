#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 20:57:59 2017

@author: yjiang
Evaluate the accuracy of the crawled web pages
"""

def gettotal(path):
    total = {}
    for line in open(path):
        text = line.split(',')
        if text[-2] not in total:
           total[text[-2]] = 1
        else:
           total[text[-2]] +=1
    
    return total

def getRele(path):
    check = {}
    for line in open(path):
        text = line.split(',')
        if 'Yes' in text[-1]:
            if text[-2] not in check:
                  check[text[-2]] = 1 
            else:
                  check[text[-2]] += 1
    return check

def getaccuracy(dic1, dic2):
    accuracy = {}
    for key in dic1:
        if key in dic2:
           accuracy[key] = dic2[key]/float(dic1[key])
        else:
           accuracy[key] = 0
    return accuracy

def getTotalNum(dic):
    num = 0
    for key in dic:
        num += dic[key]
    return num

allin = gettotal('/Users/yjiang/Documents/nutch_data/pageEva/eva_label.csv')
rele = getRele('/Users/yjiang/Documents/nutch_data/pageEva/eva_label.csv')
accuracy_dic = getaccuracy(allin, rele)

overall_accuracy = getTotalNum(rele)/float(getTotalNum(allin))


with open("output/evaluation.csv", "w") as text_file:
    for key in accuracy_dic:
        text_file.write("{0},{1}\n".format(key.replace("'",""), accuracy_dic[key]))