# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 17:56:17 2022

@author: Zachary Mark
"""

"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""
import copy

def brute_climber(n):
    #it works, but it ain't pretty
    
    #n= number of steps
    #z= number of options
    
    routes=[[0]]
    
    complete=False
    cycle=0
    while complete==False:
        for route in routes:
            if route[-1]<n-1:
                copy_route=copy.deepcopy(route)
                copy_route.append(route[-1]+2)
                routes.append(copy_route)
                route.append(route[-1]+1)
            elif route[-1]<n:
                route.append(route[-1]+1)
        
        done=True
        for route in routes:
            if route[-1]!=n:
                done=False
        if done==True:
            complete=True
        
        cycle+=1
        print(cycle)
            
    
    z=len(routes)
    
    print("Input = ",n)
    print("Output = ",z)

def top_down(n):
    """
    base cases:
        f(0)=1
        f(1)=1
        
        
    
    
    """
    
    step_list=[1,1]
    for i in range(2, n+1):
        step_list.append(step_list[-1]+step_list[-2])
        
    
    print(step_list)
    x=step_list[-1]
        
        
        
    print("Input = ",n)
    print("Output = ",x)
    
    