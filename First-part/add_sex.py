# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 16:20:26 2021

@author: pasqu
"""

from csv import writer
from csv import reader

femalesex = open('C:\\Users\\pasqu\\Desktop\\Università\\Laboratory DS\\progetto\\female_players.csv', 'r')
malesex = open('C:\\Users\\pasqu\\Desktop\\Università\\Laboratory DS\\progetto\\male_players.csv', 'r')

with open('C:\\Users\\pasqu\\Desktop\\Università\\Laboratory DS\\progetto\\player.csv', 'r') as f:
    with open('C:\\Users\\pasqu\\Desktop\\Università\\Laboratory DS\\progetto\\player_wsex.csv', 'w', newline='') as out:
        
        writer = writer(out)
        writer.writerow(['player_id','name','hand','ht','country_id','byear_of_birth','sex'])
        next(f)        
        reader = reader(f)
        

        female_name = []
        male_name = []
        
        for row in femalesex:
            row = row.replace(',',' ').rstrip('\n')
            female_name.append(row)
        
        for row in malesex:
            row = row.replace(',',' ').rstrip('\n')
            male_name.append(row)
        
        female_name.remove(female_name[0])
        male_name.remove(male_name[0])
        
        female_name = set(female_name)
        male_name = set(male_name)
        
        
        for line in reader:
            if line[1] in female_name:
                line.append('female')
            elif line[1] in male_name:
                line.append('male')
            else:
                line.append('null')
                
            writer.writerow(line)
                
        
        
        
        

            
        
                    
        

       
 
