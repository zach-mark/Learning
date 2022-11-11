# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:25:34 2022

@author: Zachary Mark
"""

"""
Lesson 30

Section 11: Files.

Filename and absolute/relative file paths
"""

import os

string_path=os.path.join('folder1', 'folder2')

print(string_path)


current_direct=os.getcwd()

print(current_direct)


"""
functions:
    
    exists
    isfile
    isdir
    
    
    getsize()- returns size in bits

"""