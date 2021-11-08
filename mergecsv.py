# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 15:58:23 2021

@author: pasqu
"""
import csv 

w = open('C:\\Users\\pasqu\\Desktop\\Università\\Laboratory DS\\progetto\\winners_modified.csv', "a")
l = open('C:\\Users\\pasqu\\Desktop\\Università\\Laboratory DS\\progetto\\losers_modified.csv', "r")

for line in l:
   w.write(line)

w.close()
l.close()
