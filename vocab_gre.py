#import pandas as pd
import os
from re import S
import time
import argparse
import random
import math
import json

class wordbank:
    def __init__(self,file):
        self.data = json.load(open(file))
        self.fname = file
    
    def add(self,new_word):
        ##TODO: the word exists already
        if new_word.key in self.data.keys():
            pass

        indices = ['考法'+str(i+1) for i in range(len(new_word.meanings))]
        definitions = [new_word.meanings[i].data for i in range(len(new_word.meanings))]
        self.data[new_word.key] = dict(zip(indices,definitions))
        with open(self.fname,'w',encoding='utf-8') as file:
            json.dump(self.data,file,ensure_ascii=False,indent=4)

class word:
    def __init__(self,key):
        self.key = key
        self.meanings = []

    def define(self):
        defi = definition()
        defi.define()
        self.meanings.append(defi) 


class definition:
    def __init__(self):
        self.data = dict(zip(['[中]','[英]','[近]','[反]','[例]','[备注]'],['']*6))
        """
        self.cn = ''
        self.en = ''
        self.eg = ''
        self.syn = ''
        self.ant = ''
        self.comments = ''
        """

    def define(self):
        cn = input("Enter Chinese Definition: ")
        en = input("Enter English Definition: ")
        syn = input("Enter synonyms, separated with commas: ")
        ant = input("Enter antonyms, separated with commas: ")
        eg = input("Enter example sentence: ")
        comments = input("Enter comments: ")
        self.data['[中]'] = cn if cn else ''
        self.data['[英]'] = en if en else ''
        self.data['[近]'] = syn if syn else ''
        self.data['[反]'] = ant if ant else ''
        self.data['[例]'] = eg if eg else ''
        self.data['[备注]'] = comments if comments else ''

    def show(self,key):
        if self.data[key]:
            return ' '.join([key,self.data[key]])

    def __repr__(self):
        output = []
        for key in self.data.keys():
            if self.data[key]:
                output.append(' '.join([key,self.data[key]]))
            #output.append(self.show(key))
        return '-------------\n'+'\n'.join(output)          
        #print()

def helper1():
    pass

def helper2():
    pass

def main():
    pass

main()