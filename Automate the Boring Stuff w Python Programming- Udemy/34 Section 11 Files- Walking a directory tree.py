# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 19:39:44 2022

@author: Zachary Mark
"""

import os

for folderName, subFolders, fileNames in os.walk('delicious'):
    print('The folder is '+folderName)
    print('The subfolders in '+ folderName+ ' are: ' + str(subFolders))
    print('The files in '+ folderName+ 'are: ' + str(fileNames))
    print()
    
    #delete all fish related folders
    for subfolder in subFolders:
        if 'fish' in subfolder:
            os.rmdir(subfolder)
            
        