# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:16:31 2023

@author: odehm
"""

#Write a program to find the shortest path between two nodes in a graph  
def shortest_path(graph, start, end):
    explored = []
     
    
    queue = [[start]]#queue for travel in the graph
     
    if start == end:
        print("Same Node")#if we reach the node
        return
     
  
    while queue:   #loop to travel between the nodes
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]#check if we visit this node
             

            for neighbour in neighbours: #loop to get to all the nighbours in the node
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
               
                if neighbour == end:
                    print("the Shortest path = ", *new_path)#check if we fet to the target node
                    return
            explored.append(node)
 
 
    print("path not exist")
    return
 
def main():
     

    graph = {'A': ['B', 'E', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B', 'E'],
            'E': ['A', 'B', 'D'],
            'F': ['C'],
            'G': ['C']}
     

    shortest_path(graph, 'A', 'D')
if __name__ == "__main__":
     main()     