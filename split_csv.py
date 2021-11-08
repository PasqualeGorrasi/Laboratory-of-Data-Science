# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 17:16:24 2021

@author: pasqu
"""


columns=[0,5,1,2,3,4,47,48]

with open('C:\\Users\\pasqu\\Desktop\\Università\\Laboratory DS\\progetto\\tournamenti.csv', 'w') as out:
    with open('C:\\Users\\pasqu\\Desktop\\Università\\Laboratory DS\\progetto\\tennis.csv', 'r')as f:
        count = 0
        max_col = float('-inf')
        min_col = float('inf')
        for line in f:
            count +=1
            tokens = line.strip().split(',')
            new_line = ''
            for col in columns:
                new_line+=tokens[col] + ','
            new_line = new_line[:-1] + "\n"
            out.write(new_line)
            max_col = max(max_col, len(tokens))
            min_col = min(min_col, len(tokens))
        print(count, max_col, min_col)
