# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 16:17:26 2022

@author: aymer
"""

fichier = open("premiers.txt", "r", encoding="utf-8")
somme = 0
L = fichier.readlines()
liste_premier = []
for ligne in L:
    nombre = ""
    for element in ligne:
        if element != "\n":
            nombre = nombre + element
    liste_premier .append(int(nombre))
print(liste_premier)