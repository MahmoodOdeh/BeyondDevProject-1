# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:40:20 2023

@author: odehm
"""

#Write a program to find the lowest common ancestor of two nodes in a binary tree.


class tree:

	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def lowest_common_ancestor(root, n1, n2):

	if root is None:
		return None

	if root.key == n1 or root.key == n2:
		return root

	
	left = lowest_common_ancestor(root.left, n1, n2)
	right = lowest_common_ancestor(root.right, n1, n2)

	if left and right:
		return root
    
	return left if left is not None else right


def main():
    
    """
    #### another tree to check not balanced ######
    root = tree(1)
    root.left = tree(2)
    root.left.left = tree(3)
    root.left.left.left = tree(4)
    print("lowest common ancestor is: ", lowest_common_ancestor(root, 2, 1).key)
	"""
    
    root = tree(1)
    root.left = tree(2)
    root.right = tree(3)
    root.left.left = tree(4)
    root.left.right = tree(5)
    root.right.left = tree(6)
    root.right.right = tree(7)
    
    print("lowest common ancestor is: ", lowest_common_ancestor(root, 6, 7).key)
   
	
    
if __name__ == "__main__":
     main() 