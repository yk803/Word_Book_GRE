from termcolor import colored,cprint
import json
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('keyword',
                    default='',type=str,
                    )       
parser.add_argument('--fname',
                    default='词表.json',type=str,
                    )       

args = parser.parse_args()

data = json.load(open(args.fname,encoding='utf-8'))


def regular_print(definitions):
    for definition in definitions.keys():
        print(definition)
        for meanings in definitions[definition].keys():
            if definitions[definition][meanings] != '':
                print(meanings,definitions[definition][meanings],sep=': ')
    print()

def print_helper_word(keyword,word):
    ind = word.find(keyword)
    print(word[:ind],end='')
    cprint(keyword,'grey','on_yellow',end='')
    print(word[ind+len(keyword):])


def print_helper_defs(keyword,defi):
    for key in defi.keys():
        if defi[key] == '':
            continue
        if not keyword in defi[key]:
            print(key,defi[key],sep=': ')
        else:
            print(key+': ',end='')
            key_indices = defi[key].find(keyword)
            print(defi[key][:key_indices],end='')
            cprint(keyword,'grey','on_yellow',end='')
            print(defi[key][key_indices+len(keyword):])
    print()

#word_printed = False

for word in data.keys():
    word_printed = False
    if args.keyword in word:
        print_helper_word(args.keyword,word)
        word_printed = True
        regular_print(data[word])
        continue

    for definition in data[word].keys():
        for meanings in data[word][definition].keys():
            #print(data[word][definition][meanings])
            if args.keyword in data[word][definition][meanings]:
                if not word_printed:
                    print(word)
                print(definition)
                print_helper_defs(args.keyword,data[word][definition])