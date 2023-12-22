# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:39:06 2023

@author: odehm
"""

#Recursion:
#Write a program to calculate the factorial of a number using recursion.

def factorialnumber(number):
    if number<0:
        return -1
    elif number == 0:
        return 1
    elif number >= 1 :
        return number *factorialnumber(number-1)
  



def main():
    number = 10
    answer = factorialnumber(number)
    if answer ==-1:
        print("the number is given is negative")
    else:
        print("the factorial number of  " + str(number) + " is : " + str(answer))
if __name__ == "__main__":
    main() 