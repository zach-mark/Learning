# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 21:47:03 2022

@author: Zachary Mark

14 Section 6

For Loops with Lists
Multiple Assignment
Augmented Assignment Operators
"""


for i in [0,1,2,3]:
    print(i)
    
list_A=["Apple","Banana","Pear","Pineapple"]

for i in list_A:
    print(i)
    
for i in range(len(list_A)):
    print("Index "+str(i)+" in list_A is: "+ list_A[i])


#use a range to build a list
example_list=list(range(0,100,2))

print(example_list)


#multiple variable assignment


cat=['fat', 'orange', 'loud', 'lazagna']
size, color, disposition, food=cat

size, color, disposition, food='fat', 'orange', 'loud', 'lazagna'
#both work

print(size, color, disposition, food)


#augmented assignment operators, this is
"""
+=
-=
*=
/=
%=
"""