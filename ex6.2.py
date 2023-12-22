# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:25:37 2023

@author: odehm
"""

#Implement the binary search algorithm.


def binarysearch(arr,target):
    
    l=0;
    r=len(arr)
    while l <= r:
        middle=int((l+r)/2) # take the middle element in the array
        if  arr[middle]==target:
            return True
        elif arr[middle] < target:  #if the target is greater we ignore the left half
            l = middle +1
        elif arr[middle] > target:  #if the target smaller we ignore the right half
            r = middle -1
    return False


def main():
    arr = [ 2,3,5,6,8,22,56]
    target =10
    answer =  binarysearch(arr, target)
    if answer :
        print ("the value  " +str(target)+ " is found")
    else :
        print ("the value  " +str(target)+ " is not found")
if __name__ == "__main__":
    main() 