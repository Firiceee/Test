# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 20:14:07 2023

@author: aymer
"""
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

def trace_grand(f,uo,mine,maxe,xmax,xmin):
    liste_terme=[0]*(maxe+1)
    liste_terme[0]=uo
    for i in range(maxe):
        liste_terme[i+1]=f(liste_terme[i])
    abscisse=[liste_terme[mine],liste_terme[mine]]
    ordonne=[liste_terme[mine]]
    for i in range(mine+1,maxe):
        abscisse.append(liste_terme[i])
        ordonne.append(liste_terme[i])
        abscisse.append(liste_terme[i])
        ordonne.append(liste_terme[i])
    ordonne.append(liste_terme[maxe])
    plt.grid("True")
    plt.xlabel("abscisse")
    plt.ylabel("ordonne")
    plt.plot([xmin,xmax],[xmin,xmax])
    plt.plot(abscisse,ordonne)
    tableau_numpy=np.linspace(xmin,xmax,200)
    trie=sorted(liste_terme[mine:maxe])
    fct_trie=[f(x) for x in trie]
    plt.plot(trie,fct_trie)
    
def chaos(r):
    f= lambda x:r*x*(1-x)
    liste_terme=[0]*(1000+1)
    liste_terme[0]=0.2
    liste_finale=[]
    for i in range(1000):
        liste_terme[i+1]=f(liste_terme[i])
    for i in range(500,1001):
        liste_finale.append(int(liste_terme[i]*512))
    return(liste_finale)

def trace_chaotique():
    r=[2.9+i/1024 for i in range(1024)]
    liste_termes=[]    
    for element in r: 
        liste_termes.append(chaos(element))
    red = (150,15,15)
    image = Image.new("RGB", (1024,512))
    for i in range(1024):
        for element in liste_termes[i]:
            image.putpixel((i,element),red)

    image.show()        
    
    