# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 16:39:51 2022

@author: aymer
"""

def appartient(x,c):
    for i in range(len(c)):
        if c[i] == x:
            return True
    return False

def appartien_2(x,c):
    for element in c:
        if element == x:
            return True
    return False

def Indice(x,c):
    for i in range(len(c)):
        if c[i] == x:
            return i
    
def les_positions(x,c):
    liste_pos= []
    for i in range(len(c)):
        if c[i] == x:
            liste_pos . append(i)
    return liste_pos

extrait="""Anton Voyl n'arrivait pas à dormir. Il alluma. Son Jaz
marquait
minuit vingt. Il poussa un profond soupir, s'assit dans son lit,
s'appuyant sur son polochon. Il prit un roman, il l'ouvrit, il lut;
mais il n'y saisissait qu'un imbroglio confus, il butait à tout instant
sur un mot dont il ignorait la signification.
\
n Il abandonna son roman
sur son lit. Il alla à son lavabo; il m
ouilla un gant qu'il passa sur
son front, sur son cou.
\
n Son pouls battait trop fort. Il avait chaud.
Il ouvrit son vasistas, scruta la nuit. Il faisait doux. Un bruit
indistinct montait du faubourg. Un carillon, plus lourd qu'un glas, plus
sourd q
u'un tocsin, plus profond qu'un bourdon, non loin, sonna trois
coups. Du canal Saint
-
Martin, un clapotis plaintif signalait un chaland
qui passait. Sur l'abattant du vasistas, un animal au thorax indigo, à
l'aiguillon safran, ni un cafard, ni un char
ançon, mais plutôt un
artison, s'avançait, traînant un brin d'alfa. Il s'approcha, voulant
l'aplatir d'un coup vif, mais l'animal prit son vol, disparaissant dans
la nuit avant qu'il ait pu l'assaillir."""
print(len(les_positions("e", extrait)))