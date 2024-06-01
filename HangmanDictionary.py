# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 14:37:33 2023

@author: miram
"""
#Oxford dictionary for hangman

oxfordDict = {}

with open("OxfordDictionaryAnsi.txt", "r") as f:
    for line in f:
        line = line.strip().split(" ",1)
        word = ''.join(line[0:1])
        word = word.lower()
        definition = line[:2]
        print (word)
        #definition = line[1]
        print (definition)    

                #count =+ 1
        oxfordDict[word] = definition
    
    
    
   
print(oxfordDict)    