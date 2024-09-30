# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 22:23:34 2022

@author: aymer
"""

import matplotlib.pyplot as plt
import math

x = [0.1*i for i in range(21)]
y = [x[i]**2 for i in range(21)]

plt.figure("fonction carré")
plt.title("essaie")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")

plt.plot(x,y)
plt.show()


