# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 19:34:16 2023

@author: aymer
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.arange(0,5,0.001)

Y = np.cos(X)
Y2 = np.sin(X)

plt.grid(True)
plt.xlabel("absscisses")
plt.ylabel("ordonnées")

plt.plot (X,Y, "r--")
plt.plot(X,Y2, "bo")

plt.show()

def suite(u0,f,n):
    liste_indice=[0]*(n+1) # chaque case de la liste étant le n_eme terme
    liste_indice[0] = u0
    for i in range(n):
        liste_indice[i+1]=f(liste_indice[i])
    return liste_indice[n]

def suite_rec(f , u0, n, xmin, xmax):
    liste_indice=[0]*(n+2) # chaque case de la liste étant le n_eme terme
    liste_indice[0] = u0
    X=[]
    Y=[u0]
    for i in range(n+1):
        liste_indice[i+1]=f(liste_indice[i])
    for i in range(n):
        X.append(liste_indice[i])
        X.append(liste_indice[i])
        if i!=0:
            Y.append(liste_indice[i])
            Y.append(liste_indice[i])
    Y.append(liste_indice[n+1])
    plt.grid(True)
    plt.xlabel("abscisse")
    plt.ylabel("ordonnées")
    plt.plot(X,Y, "r--")
    plt.plot ( [xmin,xmax],[xmin,xmax])         
    plt.scatter(X,Y)
    plt.show()        



        