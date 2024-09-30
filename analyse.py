# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 22:01:55 2022

@author: aymer
"""
import matplotlib.pyplot as plt
import math 


def split(texte):
    mot=""
    mots=[]
    for element in texte:
        if element == "\t":
            mots .append(mot)
            mot =""
        else:
            mot += element
    mots .append(mot)
    return mots
x=[]
y=[]
z=[]
t=[]
fichier = open("les_numeros.txt",'r',encoding='utf-8')
L = fichier.readline()
L = fichier.readline()
while L != "":        
        ll = split(L)
        print(ll)
        t.append(float(ll[0]))
        x.append(float(ll[1]))
        y.append(float(ll[2]))
        z.append(float(ll[3]))
        L = fichier.readline()
        
plt.figure(100)
plt.title("le grand momment")
plt.xlabel("abscisse")
plt.ylabel("ordonne")
plt.plot(t,x, 'r--' ,t,y, 'b--', t,y, "g--", t,z,"y--")
plt.show()
    
    
            
            