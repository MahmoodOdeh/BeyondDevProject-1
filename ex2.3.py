# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:17:13 2023

@author: odehm
"""
# Write a program to detect if a linked list has a cycle.

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
             
class LinkedList:
    def __init__(self):
        self.head = None #intilize the head of linkedlist

    def insertcyclemode(self, data):
        NewNode = Node(data)      #create new node with given data
        if self.head is None:     #check if its empty and add to the beginneg
            self.head = NewNode
            return
        last_node = self.head
        while last_node.next:      # get to the end of the linked list and add anode
            last_node = last_node.next
        last_node.next = NewNode
        last_node.next.next = self.head
   
    def insert(self, data):
        NewNode = Node(data)      #create new node with given data
        if self.head is None:     #check if its empty and add to the beginneg
            self.head = NewNode
            return
        last_node = self.head
        while last_node.next:      # get to the end of the linked list and add anode
            last_node = last_node.next
        last_node.next = NewNode         
        
        
    def hasAcycle (self):
        temp= self.head
        while temp !=None:
              if temp.next == self.head :
                 return True 
              temp = temp.next
        return False        
              
    def printLinkList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")        


        
def main():
    list = LinkedList()
    list.insert(1)
    list.insert(2)
    list.insert(3)
    list.insert(4)
    list.insert(5)
    list.insert(6)
    list.insert(7)
    list.insert(8)
    #list.insertcyclemode(9)
    print("the linked list is :")
   # list.printLinkList()
    if(list.hasAcycle()):
        print("the linkedlist has acycle")
    else :
        print("the linkedlist has no cycle")
    
if __name__ == "__main__":
    main()    