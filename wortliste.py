#!/usr/bin/env python
# coding: utf8



"""
.. module:: generiere-zufallswort
   :synopsis: Generate random german words. 
.. moduleauthor:: Maximilian Freitag
"""


import random as random
import os


#read the duden.txt file
duden = ['cat', 'dog', 'Mouse', 'horse', 'Cow', 'pig', 'Sheep', 'chicken', 'duck', 'goose', 'fish', 'lizard', 'frog', 'turtle', 'snake', 'eagle', 'bird', 'deer', 'goat', 'sheep', 'pig', 'cow', 'dog', 'cat', 'mouse', 'horse', 'cow', 'pig', 'sheep', 'chicken', 'duck', 'goose', 'fish', 'lizard', 'frog', 'turtle', 'snake', 'eagle', 'bird', 'deer', 'goat', 'sheep', 'pig', 'cow', 'dog', 'cat', 'mouse', 'horse', 'cow', 'pig', 'sheep', 'chicken', 'duck', 'goose', 'fish', 'lizard', 'frog', 'turtle', 'snake', 'eagle', 'bird', 'deer', 'goat', 'sheep', 'pig', 'cow', 'dog', 'cat', 'mouse', 'horse', 'cow', 'pig', 'sheep', 'chicken', 'duck', 'goose', 'fish', 'lizard', 'frog', 'turtle', 'snake', 'eagle', 'bird', 'deer', 'goat', 'sheep', 'pig', 'cow', 'dog', 'cat', 'mouse', 'horse', 'cow', 'pig', 'sheep', 'chicken', 'duck', 'goose', 'fish', 'lizard', 'frog', 'turtle', 'snake', 'eagle', 'bird', 'deer', 'goat', 'sheep', 'pig', 'cow', 'dog', 'cat', 'mouse', 'horse', 'cow', 'pig', 'sheep', 'chicken', 'duck', 'goose', 'fish', 'lizard', 'frog', 'turtle', 'snake', 'eagle', 'bird', 'deer', 'goat', 'sheep', 'pig', 'cow', 'dog', 'cat', 'mouse', 'horse', 'cow', 'Pig', 'sheep', 'chicken', 'duck']



def zufallswort():
    #use the duden.txt file to generate a random word
    return random.sample(duden)



def zufallswoerter(n):
    return random.sample(duden, k=n)


def anfangsbuchstaben(m: str, n: int):
    a = list(filter(lambda x: x.lower().startswith(m), duden)) 
    return random.sample(a, k=n) 


def endbuchstaben(m: str, n: int):
    h = list(filter(lambda x: x.lower().endswith(m), duden)) 
    return random.sample(h, k=n)
    
    
def enthaelt_buchstaben(m: str, n: int):
      a = list(filter(lambda x: m in x.lower(), duden)) 
      return random.sample(a, k=n)   


def anzahl_buchstaben(m: int, n: int):    
    
    a = []  
    
    for i in duden:
        if len(i) == m:
            a.append(i)
     
    return random.sample(a, k=n)










#Substantive

def substantiv(n: int):
        try:
                #return only words that start with a capital letter
                a = list(filter(lambda x: x[0].isupper(), duden))
                return random.sample(a, k=n)

        except:
                ValueError
                return f"There are only {len(a)} nouns in the data set"



def substantiv_anfangsbuchstaben(m: str, n: int):
        try:
                
                a = list(filter(lambda x: x[0].isupper() and x.startswith(m), duden)) 
                return random.sample(a, k=n)
        except:
                ValueError
                return f"There are only {len(a)} nouns that start with {m}"
        



def substantiv_endbuchstaben(m: str, n: int):
        try:
                
                a = list(filter(lambda x: x[0].isupper() and x.endswith(m), duden)) 
                return random.sample(a, k=n)
        except:
                ValueError
                return f"There are only {len(a)} nouns that end with {m}"





def substantiv_enthaelt(m: str, n: int):
        try:
                a = list(filter(lambda x: m in x.capitalize(), duden))

                return random.sample(a, k=n)
        except:
                ValueError
                return f"There are only {len(a)} nouns that include {m}"




def substantiv_buchstaben(n: int, m: int):    
        try:
            
            a = list(filter(lambda x: len(x) == m and x[0].isupper(), duden))
            return random.sample(a, k=n)
        except:
            ValueError
            return f"There are only {len(a)} nouns with {m} letters"








