# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 23:30:13 2023

@author: odehm
"""

#Bit Manipulation:
#Write a program to check if a given number is even or odd using bit manipulation.

def checknumber(number):
    if number^1==number+1:
        print ("the number "+str(number)+" is even")
    else:
        print ("the number "+str(number)+" is odd")
        
        
def main():
    number=12
    checknumber(number) 
if __name__ == "__main__":
    main()       