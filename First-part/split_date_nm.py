# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 09:15:30 2021

@author: pasqu
"""

from csv import writer
from csv import reader


with open('C:\\Users\\pasqu\\Desktop\\Università\\Laboratory DS\\progetto\\date.csv', 'r') as f:
    with open('C:\\Users\\pasqu\\Desktop\\Università\\Laboratory DS\\progetto\\datesplit.csv', 'w',newline='') as out:
        
        writer = writer(out)
        writer.writerow(['date_id', 'year', 'month', 'day','quarter'])
        next(f)        
        reader = reader(f)
        
        count_id = 0
        for row in reader:

            year = int(row[0][:4])
            month = int(row[0][4:6])
            day = int(row[0][6:8])
            quarter = (month-1)//3 + 1

            row.append(year)
            row.append(month)
            row.append(day)
            row.append(quarter)
            
            writer.writerow(row)


            

            
            