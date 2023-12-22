# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:23:55 2023

@author: odehm
"""
#Linked Lists:
# Write a program to reverse a linked list.
# Write a program to find the middle element of a linked list.

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
             
class LinkedList:
    def __init__(self):
        self.head = None #intilize the head of linkedlist

    def insert(self, data):
        NewNode = Node(data)      #create new node with given data
        if self.head is None:     #check if its empty and add to the beginneg
            self.head = NewNode
            return
        last_node = self.head
        while last_node.next:      # get to the end of the linked list and add anode
            last_node = last_node.next
        last_node.next = NewNode
        
        
        
    def printLinkList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")        

    def reverseLinkedList(self):
        prev=None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev    
        
    def middleElement(self):
        count=0
        if self.head :
           node=self.head 
           while node :
                 count= count+1
                 node =node.next
           i=0
           node=self.head
           while i != int(count/2) :
               i=i+1
               node = node.next
           return node.data    
              
        
        
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
    list.insert(9)
    print("the linked list is :")
    list.printLinkList()
    print("the reversed linked list is :")
    list.reverseLinkedList()
    list.printLinkList()
    print("the midlle element is : "+str(list.middleElement()))
if __name__ == "__main__":
    main()    