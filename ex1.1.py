# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:36:53 2023

@author: odehm
"""
#Arrays and Strings:
# Write a program to reverse a string in place

def reverse_string(str):
    newstr = " "
    for ch in str:
        newstr =ch +newstr
    return newstr  
      
def main():
    str = "123456789"
    print(reverse_string(str))
if __name__ == "__main__":
    main()
    
 
      
     
     
    
    
    