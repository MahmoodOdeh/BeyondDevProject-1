# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:26:24 2023

@author: odehm
"""

#Write a program to check if a given string of parentheses is balanced.

def parenthesesBalanced(parentheses):
    stack = []
    if len(parentheses)==0:
       return -1
    if parentheses[0]==')' or parentheses[0]=='}' or parentheses[0]=='}':
       return False 
    for ch in parentheses:
        if ch=='(' or ch=='{' or ch=='[' :
           stack.append(ch)
        if not stack: #checkk stack is empty
           return False 
        else :  
            current_parentheses=stack.pop()#check if the parentheses from same type
            if current_parentheses == '(':
                if ch!=')':
                   return False
            elif current_parentheses == '{':
                if ch!='}' : 
                   return False
            elif current_parentheses == '[':
                if ch!=']' : 
                   return False   
               
    if not stack: #checkk stack is empty
        return True
    return False


def main():

    parentheses = "]"
    if parenthesesBalanced(parentheses)==-1:
       print ("empty input") 
    elif parenthesesBalanced(parentheses):
       print("parentheses is Balanced")
    else:
       print(" parentheses is not Balanced")
    
if __name__ == "__main__":
    main()            