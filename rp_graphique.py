# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 21:54:46 2022

@author: aymer
"""

import matplotlib.pyplot as plt
import numpy as np
from math import *

x = np.arange(0,2,0.001)
y = [sqrt(elt) for elt in x]

plt.figure(111)
plt.title("racine carre")
plt.xlabel("abscisse")
plt.ylabel("ordonne")
plt.plot(x,y, "b--")
plt.show()