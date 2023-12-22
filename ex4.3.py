# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:40:57 2023

@author: odehm
"""

#Implement a binary search tree and write functions to insert, delete and search for elements.
class tree:
    
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self,value):
       if self.value:
           if value<self.value:
               if self.left is None:
                   self.left=tree(value)
               else:
                   self.left.insert(value)
           elif value>self.value :
               if self.right is None:
                   self.right=tree(value)
               else:
                   self.right.insert(value)
       else: self.value=value  
       
      
       
      
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value),
        if self.right:
            self.right.PrintTree() 
           
            
           
            
    def search(self, value):
        if value==self.value:
            return str(value) #return the value if we found
        elif value < self.value: #check if the value less we go to the left
            if self.left:   #if we want to move in the left
                return self.left.search(value)
            else:
                return -1
        else:          #check if the value greater we go to the right
            if self.right:  #if we want to move in the right
                return self.right.search(value)
            else:
                return -1       
            
            
    def delete(self, val):
        if val < self.value:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.value:
            if self.right:
                self.right = self.right.delete(val)
        else:
           
            if self.left is None:  #If the node with 1 child or none
                return self.right
            elif self.right is None:
                return self.left

            
            self.data = self.right.find_min_value() #if the node with 2 childs
            self.right = self.right.delete(self.data)

        return self      
            
    def find_min_value(self):
        current = self
        while current.left:
            current = current.left
        return current.value
    


def main():
    
    root=tree(15)
    root.insert(22)
    root.insert(33)
    root.insert(14)
    root.insert(5)
    root.insert(26)
    root.insert(7)
    root.PrintTree()
    found=root.search(1)
    if(found == -1):
        print("the value is not exist: ")
    else:   
        print ("the vale is found is:  ")
    root.PrintTree()    
    print("******************************************")
    root.delete(5)
    root.PrintTree()
if __name__ == "__main__":
     main() 