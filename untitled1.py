# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 20:35:57 2023

@author: aymer
"""

def algo_horner(polynome,x):
    res=polynome[0]
    for i in range(1,len(polynome)):
        res = res*x + polynome[i]
    return res

def tri_par_maximum(liste):
    copie = liste[:]
    for j in range(len(liste)-1):
        maxi=copie[0]
        indice = 0
        for i in range(len(liste)-j):
            if copie[i] >= maxi:
                maxi = copie[i]
                indice = i
        copie[indice], copie[len(copie)-j-1] = copie[len(copie)-j-1], copie[indice]
    return copie          
            
            
            
def recherche_dicho(x,liste):
    debut = 0
    fin = len(liste) -1
    pivot =(debut+fin) //2
    while fin >= debut:
        if liste[pivot] == x:
            return True
        if liste[pivot] >= x:
            fin = pivot -1
        else:
            debut = pivot+1
 
        pivot =((fin)+debut) //2
    if liste[pivot] == x:
        return True
    return False


def autre_tri(liste):
    copie = liste[:]
    trie = []
    for j in range(len(liste)):
        trie.append(copie[j])
        while j>0:
            if trie[j]<trie[j-1]:
                trie[j] , trie[j-1] = trie[j-1], trie[j]
                j=j-1
                print(trie)
            else:
                j=0
    return trie
        

def troisieme_trie(liste):
    j=1
    while j>0:
        j=0
        for i in range(len(liste)-1):
            if liste[i] >= liste[i+1]:
                j = j+1
                liste[i],liste[i+1] = liste[i+1], liste[i]
    return liste
    
    
    
    
    