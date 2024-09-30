# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 21:43:07 2022

@author: aymer
"""

def split(texte):
    mots=[]
    mot=""
    for element in texte:
        if element == "\t" and len(mot)>=1:
            mots.append(mot)
            mot = ""
        else:
            mot = mot+element
    mots.append(mot)
    return mots

admissible = open("admissible.txt", "r", encoding = "utf-8")
liste = [0 for i in range(5)]
L = admissible.readline()
while L!= "":
    LL = split(L)
    liste[0] = liste[0]+1
    if LL[3] != "-\n":
        liste[int(LL[3])] += 1 
    L =admissible.readline()
print(liste)