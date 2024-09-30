# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 21:09:08 2022

@author: aymer
"""

def Fichier_to_str(fichier):
    a_traiter= open(fichier, 'r', encoding='utf-8')
    L1=a_traiter.readline()
    txt=""
    while L1!="":
        L1= a_traiter.readline()
        txt = txt + L1
    return txt

def compte_mot_2_lettre(texte):
    dico = {}
    mot=""
    for i in range(len(texte)):
        if len(mot) >=2:
            if mot in dico:
                dico[mot]+=1
            elif mot[::-1] in dico:
               dico[ mot[::-1]] +=1
            else:
                dico[mot] = 1
            mot=""
        if texte[i]!="\n":
            mot = mot+texte[i]
    return dico

def compte_mot_k_lettre(texte,k):
    dico = {}
    mot=""
    for i in range(len(texte)):
        if len(mot) >=k:
            if mot in dico:
                dico[mot]+=1
            elif mot[::-1] in dico:
               dico[ mot[::-1]] +=1
            else:
                dico[mot] = 1
            mot=""
        if texte[i]!="\n":
            mot = mot+texte[i]
    return dico

def Maxi_dico(dictionnaire):
    maxe=-1
    maxi = []
    for cle,valeur in dictionnaire.items():
        if int(valeur) > maxe:
            maxe = valeur
            maxi = [cle]
        elif valeur == maxe:
            maxi .append(cle)
    return maxi
        