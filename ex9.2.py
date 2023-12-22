# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 23:34:36 2023

@author: odehm
"""

#Write a program to find the number of set bits in a given integer using bitmanipulation.

def numberofsetbits(number):
    if number  < 0:
        return -1
    count=0
    while number !=0:
        number &= (number-1)
        count += 1
    return count    
        
        
        
def main():
    number= 10
    numbersets=numberofsetbits(number)
    if numbersets ==-1:
        print("the number " +str(number)+ " is negative")
    else : 
        print("the number of set bits in " +str(number)+ "  is : " + str(numbersets))
if __name__ == "__main__":
    main()   