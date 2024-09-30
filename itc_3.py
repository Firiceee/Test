# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 20:22:10 2022

@author: aymer
"""

import time

def exp(a,n):
    return a**n
def exp_rec(a,n):
    if n==0:
        return(1)
    else:
        return(a*exp_rec(a, n-1))

def expo_rapide(a,n):
    q=n
    puis=a
    res=1
    while q>0:
        if q%2 ==1:
            res = res * puis
        q = q//2
        puis = puis * puis
    return res
            