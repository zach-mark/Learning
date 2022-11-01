# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 16:38:02 2022

@author: Zachary Mark
"""


"""
Section 7. Dictionaries
Video 18- Data Structures

"""


cat={'name':'Zophie', 'age':7, 'color': 'Black'}

allCats=[]
allCats.append(cat)
allCats.append({'name':'Stray', 'age':2, 'color': 'Orange'})

print(allCats)



the_Board={'Top-L': 0,'Top-M': 0,'Top-R': 0,
           'Mid-L': 0,'Mid-M': 0,'Mid-R': 0,
           'Bot-L': 0,'Bot-M': 0,'Bot-R': 0
           }

def printBoard(board):
    print(board['Top-L'],'|',board['Top-M'],'|',board['Top-R'])
    print("__________")
    print(board['Mid-L'],'|',board['Mid-M'],'|',board['Mid-R'])
    print("__________")
    print(board['Bot-L'],'|',board['Bot-M'],'|',board['Bot-R'])