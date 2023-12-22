# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:51:34 2023

@author: odehm
"""

#Write a program to generate all permutations of a string using recursion


def toString(lst):
    result = ''
    for char in lst:
        result += char
    return result


def permutations(lst,start,length):
    
    if start==length:
        print(toString(lst))
    for i in range (start,length):
        lst[start],lst[i]=lst[i],lst[start]
        permutations(lst, start+1, length)
        lst[i],lst[start]=lst[start],lst[i]

def main():
        
    string = 'abc'
    length = len(string)
    lst= list(string)
    start = 0
    permutations(lst,start,length)
if __name__ == "__main__":
    main() 