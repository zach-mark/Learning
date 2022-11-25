# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 21:29:37 2022

@author: Zach
"""


"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2
of size m and n respectively, return the median
of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

def array_medians(array_1, array_2):
    m=len(array_1)
    n=len(array_2)
    
    
    
    merged_array=[]
    
    
    """
    both lists are sorted, but they may have overlap
    
    Find out if they do
    """
    
    a_1_start=array_1[0]
    a_1_end=array_1[-1]
    
    a_2_start=array_2[0]
    a_2_end=array_2[-1]
    
    
    if a_1_start>a_2_end:
        #all of Array 1 is larger than Array 2.
        final_array=array_2+array_1
    
    elif a_1_end<a_2_start:
        #all of Array 2 is larger than Array 1.
        final_array=array_1+array_2
    
    else:
        #the arrays have overlap.
        
        a_1_tick=0
        a_2_tick=0
        final_array=[]
        run_over=False
        while run_over==False:
            if array_1[a_1_tick]>array_2[a_2_tick]:
                final_array.append(array_2[a_2_tick])
                a_2_tick+=1
            else:
                final_array.append(array_1[a_1_tick])
                a_1_tick+=1
                
            
            if a_1_tick==m:
                run_over=True
                final_array=final_array+array_2[a_2_tick:]
            elif a_2_tick==n:
                run_over=True
                final_array=final_array+array_1[a_1_tick:]
                
    
    print("merged array: ",final_array)
    
    med= median(final_array)
    
    print("median: ", med)
    
    return med
                
        
        
        


def median(num_array):
    a_len=len(num_array)
    if a_len%2==0:
        
        mid_1=num_array[int(a_len/2)]
        mid_2=num_array[int(a_len/2-1)]
        
        med=(mid_1+mid_2)/2
    else:
        samp=int(a_len/2)
        
        med=num_array[samp]
        
    return med
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    