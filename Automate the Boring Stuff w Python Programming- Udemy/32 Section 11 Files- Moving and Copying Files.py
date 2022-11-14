# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 19:24:39 2022

@author: Zachary Mark
"""

"""
Lesson 32 and 33

32- copying and moving files

33- deleting files
"""
#'sh' Util
import shutil

#simple copy
#shutil.copy("bacon.txt", "files_examples")

#copy and rename
#shutil.copy("bacon.txt", "files_examples\\tasty_food.txt")

#copying a whole group of files

#shutil.copytree("files_examples","files_examples_backup")

#simple move
#shutil.move()

#to rename, just use MOVE with a new name


"""
deleting files
"""

import os

#os.unlink()
#deletes a file


#os.rmdir()
#deletes a folder
#will not work if it is not empty.

import shutil
#shutil.rmtree()
#deletes a folder and all contents

for filename in os.listdir():
    print(filename)
    
"""
All these deleting are v dangerous, send to trash might be better.
send2trash
pip install 
"""