# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 19:24:39 2022

@author: Zachary Mark
"""


#'sh' Util
import shutil

#simple copy
shutil.copy("bacon.txt", "files_examples")

#copy and rename
shutil.copy("bacon.txt", "files_examples\\tasty_food.txt")

#copying a whole group of files

shutil.copytree("files_examples","files_examples_backup")

#simple move
#shutil.move()

#to rename, just use MOVE with a new name
