# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 10:49:42 2021

@author: pasqu
"""

from csv import writer
from csv import reader

with open('C:\\Users\\pasqu\\Desktop\\Università\\Laboratory DS\\progetto\\match.csv', 'r') as f:
    with open('C:\\Users\\pasqu\\Desktop\\Università\\Laboratory DS\\progetto\\match_conid.csv', 'w',newline='') as out:
        
        writer = writer(out)
        writer.writerow(['tourney_id','match_id','winner_id','loser_id','score','best_of','round','minutes','w_ace','w_df','w_svpt','w_1stIn','w_1stWon','w_2ndWon','w_SvGms','w_bpSaved','w_bpFaced','l_ace','l_df','l_svpt','l_1stIn','l_1stWon','l_2ndWon','l_SvGms', 'l_bpSaved','l_bpFaced' ,'winner_rank', 'winner_rank_points' ,'loser_rank', 'loser_rank_points'])
        next(f)        
        reader = reader(f)
        
        num = 0
        torneo = 0
        for row in reader:
            if row[0]!=torneo:
                num = 0
            num+=1
            torneo = row[0]
            
            match_id = str(num)+'-'+ torneo
            row.insert(1, match_id)
            
            writer.writerow(row) 
        
        