# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:03:07 2023

@author: odehm
"""
#Write a program to find the maximum and minimum elements in an array
    
def find_max_min(arr):
    min=arr[0]
    max=arr[0]
    for i in range (1,len(arr)):
        if min > arr[i]:
           min = arr[i] 
        if max < arr[i]:
           max = arr[i]
    print(min) 
    print(max)      
    
def main():
    arr = [ 2,-3,63,8,5,3,5,22,77,56 ,-1]
    find_max_min(arr)
if __name__ == "__main__":
    main()    