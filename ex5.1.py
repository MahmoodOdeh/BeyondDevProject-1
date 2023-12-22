# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:37:09 2023

@author: odehm
"""

#Sorting Algorithms:
#Implement the bubble sort algorithm.



def bubblesort(arr):
    if len(arr)<=1:
        return arr
    for i in range (1,len(arr)):
        for j in range (0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr            
           
    
def main():
    arr = [ 2,-3,63,8,5,3,5,22,77,56 ,-1]
    print(bubblesort(arr))
if __name__ == "__main__":
    main()     
