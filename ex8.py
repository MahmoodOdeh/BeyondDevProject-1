# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 23:03:03 2023

@author: odehm
"""

#Hash Tables:
# Implement a hash table and write functions to insert, delete, and search for elements.

class hashtable: 
	def __init__(self, key, value): 
		self.key = key 
		self.value = value 
		self.next = None


class HashTable: 
	def __init__(self, capacity): 
		self.capacity = capacity 
		self.size = 0
		self.table = [None] * capacity 

	def _hash(self, key): 
		return hash(key) % self.capacity 

	def insert(self, key, value): 
		index = self._hash(key) 

		if self.table[index] is None: 
			self.table[index] = hashtable(key, value) 
			self.size += 1
		else: 
			current = self.table[index] 
			while current: 
				if current.key == key: 
					current.value = value 
					return
				current = current.next
			new_node = hashtable(key, value) 
			new_node.next = self.table[index] 
			self.table[index] = new_node 
			self.size += 1

	def search(self, key): 
		index = self._hash(key) 

		current = self.table[index] 
		while current: 
			if current.key == key: 
				return current.value 
			current = current.next

		raise KeyError(key) 

	def remove(self, key): 
		index = self._hash(key) 

		previous = None
		current = self.table[index] 

		while current: 
			if current.key == key: 
				if previous: 
					previous.next = current.next
				else: 
					self.table[index] = current.next
				self.size -= 1
				return
			previous = current 
			current = current.next

		raise KeyError(key) 

 

	def __contains__(self, key): 
		try: 
			self.search(key) 
			return True
		except KeyError: 
			return False


# Driver code 
if __name__ == '__main__': 

	ht = HashTable(5) # Create a hash table with a capacity of 5 

	
	ht.insert("apple", 3) 
	ht.insert("banana", 2) #add keys to the hashtable
	ht.insert("cherry", 5) 

	
	print("apple" in ht) # 
	print("durian" in ht) # checking if the hashtable have the keys

 
	print(ht.search("banana")) #get the value for the key


	ht.insert("banana", 4) 
	print(ht.search("banana")) #update the value for the key

	ht.remove("apple") 


