# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 16:30:28 2022

@author: aymer
"""

joueur_de_tennis = open("tennis.txt", 'r', encoding='utf-8')



def split(texte):
    chaines = []
    chaine = ""
    for i in range(len(texte)):
        if texte[i]!=',' and texte[i]!="\n":
            chaine = chaine + texte[i]
        elif len(chaine)>=1:
            chaines.append(chaine)
            chaine = ""
    chaines .append(chaine)
    return chaines
            
            
def moyen(fichier):
    L = fichier.readline()
    L = fichier.readline()
    compteur = 0
    moyenne = 0
    while len(L)>=4:
        print(L)
        LL = split(L)
        moyenne += int(LL[3])
        compteur += 1
        L = fichier.readline()
    return moyenne/compteur