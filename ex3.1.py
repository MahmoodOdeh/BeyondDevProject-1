# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:45:43 2023

@author: odehm
"""

#Stacks and Queues:
# Implement a stack using two queues.

from _collections import deque


class stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
        
    def push(self,x):
        self.q2.append(x)
        
        
        while self.q1:
            self.q2.append(self.q1.popleft()) #move all elements from q1 to q2
            
        self.q1, self.q2 = self.q2, self.q1 #swap q1 and q2 
            
    def pop(self):
        if self.q1:
           self.q1.popleft()
           
    def top (self):
        if(self.q1):
           return self.q1[0]
        return None
    
    def size(self):
        return len(self.q1)
    
def main():
    
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print("size is :" +str(s.size()))
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())

    print("current size: ", s.size())
    
    
if __name__ == "__main__":
    main()

         
            
        