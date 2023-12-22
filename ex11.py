# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:42:36 2023

@author: odehm
"""
#Suppose you have a grid of n x m cells, where each cell is either empty or contains a
#rock. You're given a starting position in the grid (x,y), and you want to reach a target
#position (tx,ty), but you can only move in four directions (up, down, left, right) and you
#can only move through empty cells.You're also given a limited number of moves k
#that you can make. Write a program to determine if it's possible to reach the target
#position from the starting position within k moves


import heapq

def gridToGraph(grid):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # set directions (up, down, left, right)
    n = len(grid)
    m = len(grid[0])
    graph = {}

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                graph[(i, j)] = {}
                for tx, ty in directions:
                    nx = i + tx
                    ny = j + ty
                    if nx >=0 and nx < n and ny >=0 and ny < m and grid[nx][ny]==0:
                        graph[(i, j)][(nx, ny)] = 1  # for every valid neighbor we put 1 

    return graph

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def main():
    grid = [
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 0, 0]
    ]
    
    k= 5
    start = (0,0)  # Starting position as tuple (x, y)
    target= (2,2)
    if (k < 0):
        print("please enter positive moves") #check if the moves is positive number
        return 
    if not (0 <= start[0] and start[0] < len(grid) and 0 <= start[1] and start[1] < len(grid[0]) and grid[start[0]][start[1]] == 0):
      print("we cant start at this point") #check if we can start  at this cordinates
      return

    if not (0 <= target[0] and target[0] < len(grid) and 0 <= target[1] and target[1] < len(grid[0]) and grid[target[0]][target[1]] == 0):
      print("we cant get to this point") #check if we can reach this cordinates
      return
    graph = gridToGraph(grid)
    result = dijkstra(graph, start)
    if result[target] <= k:
        print("true")
    else :
        print("false")

if __name__ == "__main__":
    main()
