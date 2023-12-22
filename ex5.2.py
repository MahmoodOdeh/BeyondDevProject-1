# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:48:05 2023

@author: odehm
"""
#• Implement the merge sort algorithm.


def mergesort(arr):
    if len(arr)<=1:
        return arr
    arr1=arr[0:int(len(arr)/2)]
    arr2=arr[int(len(arr)/2):]
       
    arr1=mergesort(arr1)
    arr2=mergesort(arr2)
    
    return merge(arr1,arr2)

def merge(arr1, arr2):
    arraysorted = []
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] > arr2[0]:
            arraysorted.append(arr2[0])
            arr2.remove(arr2[0])
        else:
            arraysorted.append(arr1[0])
            arr1.remove(arr1[0])
    
    while len(arr1) !=0 :
           arraysorted.append(arr1[0])
           arr1.remove(arr1[0])
           
    while len(arr2) !=0 :
            arraysorted.append(arr2[0])
            arr2.remove(arr2[0]) 
    return arraysorted        

def main():
    arr = [ 2,-3,63,8,5,3,5,22,77,56 ,-1]
    print(mergesort(arr))
if __name__ == "__main__":
    main()   