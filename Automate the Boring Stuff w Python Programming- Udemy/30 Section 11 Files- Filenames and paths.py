# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:25:34 2022

@author: Zachary Mark
"""

"""
Lesson 30 and 31

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







#text editing.
#bin, txt, py files.

hello_file=open('C:\\Users\\zsm54\\Documents\\GitHub\\Learning\\Automate the Boring Stuff w Python Programming- Udemy\\hello.txt')
content=hello_file.read()
list_content=hello_file.readlines()

hello_file.close()

new_file= open('C:\\Users\\zsm54\\Documents\\GitHub\\Learning\\Automate the Boring Stuff w Python Programming- Udemy\\files_text_example_00.txt', 'w')

for i in range(0,3):
    new_file.write('Hello!!!!! \n')
new_file.write('Goodbye.')
new_file.close()


new_file_2=open("files_text_example_01.txt", "w")
new_file_2.write("Bacon is not a vegetable")
new_file_2.close()

new_file_2=open('bacon.txt', 'a')
new_file_2.write("\n\nBacon is delicious.")
new_file_2.close()



"""
the shelve module
"""
import shelve

shelfFile=shelve.open('mydata')
shelfFile['cats'] = ["Zophie", "Pooka", "Simon", "Fat-Tail", "Cleo"]
shelfFile.close()

#very similar to dictionaries



