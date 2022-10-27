# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 21:38:33 2022

@author: Zachary Mark
"""

"""
Section 6. Lists
Video 13- The List Data Type
value containing multiple values,
values in lists are called items
items in lists start with indexes at 0
negative indexes work from the end of the list

"""

#begins and ends with square brackets. comma separated

list_1=['cat','dog','mouse','rat']

print(list_1)

print(list_1[0])

list_2=[[33,33],[13,12],[44,63]]

print(list_2[1][0])

list_2[1]="Dog"

print(list_2)


list_2[1:3]=["Car", "Truck"]
print(list_2)

list_3=[1,2,3,4,5]

list_3[2:]=[44,33,1,232,111,1,1,1,111,11]
print(list_3)

if 232 in list_3:
    print("wow")