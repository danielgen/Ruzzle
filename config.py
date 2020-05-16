# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:32:13 2020

@author: genti
"""
# define function to load vocabulary list of words
def get_vocabulary(filename="language_files\italian_vocab.txt"):
    with open(filename, "r") as file:
        WORDS = [line.replace("\n","") for line in file.readlines()]
        WORDS = [w for w in WORDS if 2 <= len(w) <= 16]
        
        return WORDS

# check a start point until either the word path is interrupted or word is found
def check(word, point, pos, path, father):
    if pos < len(word):
        # check current letter
        letter = word[pos]
        path[pos] = []
        for direction, cell in point.loc.items():
            if cell and cell.contains(letter) and cell not in father:
                path[pos].append(cell)
                if pos == len(word)-1:
                    # if letter is found and letter is last letter of word then return
                    father.append(point)
                    father.append(cell)
                    return father

        # if letter was not found 
        if not path[pos]:
            pass
        
        # if letter is found but it is not the last one of the word, recursive
        else:
            new_pos = pos + 1
            father.append(point)
            for cell in path[pos]:
                found = check(word, cell, new_pos, path, father)
                if found:
                    return found
                
      