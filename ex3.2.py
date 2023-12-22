# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:22:21 2023

@author: odehm
"""

#Implement a queue using two stacks

class queue:
    
    def __init__(self):
        self.s1=[]
        self.s2=[]
        
        
    def enqueue(self,x):      
        while len(self.s1) != 0: #move all elements to stack2
            self.s2.append(self.s1[-1])
            self.s1.pop()      
           
        
        #push x to stack1
        self.s1.append(x)
        
        
        while len(self.s2) != 0: #move all elements to stack1
            self.s1.append(self.s2[-1]) 
            self.s2.pop()
            
    def dequeue(self):
         
         if len(self.s1)==0:#check if stack is empty
             return -1
         
            #return the top of the stack
         x=self.s1[-1]
         self.s1.pop()
         return x
     
def main():
    q = queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    

if __name__ == "__main__":
    main()            