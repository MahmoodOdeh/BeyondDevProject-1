# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 18:23:10 2023

@author: odehm
"""
#Write a program to remove duplicates from a sorted array.
def remove_duplicates(arr,length):
    if length == 0 or length ==1 :
       return length 
    j = 0
    
    for i in range (length-1):
        if arr[i] != arr[i+1]:
           arr[j]=arr[i]
           j+=1
    arr[j]=arr[length-1]   
    return j +1
      
def main():
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    n=len(arr)
    n=remove_duplicates(arr,n)
    for i in range (n):
        print(arr[i],end=" ")
if __name__ == "__main__":
    main()  
    