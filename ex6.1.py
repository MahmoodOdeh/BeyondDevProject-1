# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:06:10 2023

@author: odehm
"""
#Searching Algorithms:
# Implement the linear search algorithm.

def linearsearch(arr,target):
    
    for i in range (0,len(arr)):
        if arr[i]==target:
            return True
    else:
        return False

def main():
    arr = [ 2,-3,63,8,5,3,5,22,77,56 ,-1]
    target = 5
    answer = linearsearch(arr, target)
    if answer :
        print ("the value  " +str(target)+ " is found")
    else :
        print ("the value  " +str(target)+ " is not found")
if __name__ == "__main__":
    main() 