# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 22:07:15 2022

@author: aymer
"""

hamlet = open("hamlet.txt", 'r')
L = hamlet.readline()

def split(texte):
    mots = []
    mot = ""
    for element in texte:
        if element == " " and len(mot)>=1:
            mots.append(mot)
            mot=""
        mot = mot+element
    mots.append(mot)
    return mots
dico = {}
while L != "":
    LL = split(L)
    if LL[0][len(LL[0])-1] == ".":
        if LL[0] in dico:
            dico[LL[0]] += 1
        else:
            dico[LL[0]] = 1
    L = hamlet.readline()
print(dico)        
            
            