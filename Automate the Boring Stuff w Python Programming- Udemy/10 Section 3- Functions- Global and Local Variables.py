"""
Created on Wed Oct 26 19:48:00 2022

@author: Zachary Mark
"""

"""
local variable is within a function
global variable is within the entirity of the code

local variables turn functions into black boxes, where you can name any 
variable whatever you like
"""

x=333
y=222
z=111

def example():
    x=11
    print(x) #this will print 11
    
    
def example_2():
    global x
    print(x)#this will print 333
    

def global_test():
    global egg
    egg=99

global_test()

print(egg)