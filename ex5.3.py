# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 19:36:11 2023

@author: odehm
"""

#Implement the quicksort algorithm.

def quicksort(arr):
   if len(arr)<=1:
       return arr
   pivot =arr.pop(int(len(arr)/2))# choose the pivot 
   left =[]
   right=[]
   for i in arr:
       if i < pivot:
           left.append(i)
       else: right.append(i)
       
   return quicksort(left) + [pivot] + quicksort(right)           
           
    
def main():
    arr = [ 2,-3,63,8,5,3,5,22,77,56 ,-1]
    print(quicksort(arr))
if __name__ == "__main__":
    main() 