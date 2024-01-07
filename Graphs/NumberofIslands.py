'''Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.'''
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        for row_index in range(len(grid)):
            for col_index in range(len(grid[row_index])):
                if grid[row_index][col_index] == "1":
                    number_of_islands += 1
                    queue = []
                    queue.append((row_index,col_index))
                    while len(queue)!=0:
                        island_row,island_col = queue.pop()
                        grid[island_row][island_col] = "0"
                        if island_col!= len(grid[row_index])-1 and grid[island_row][island_col+1]=="1":
                            queue.append((island_row,island_col+1))
                        if island_row!=len(grid)-1 and grid[island_row+1][island_col]=="1":
                            queue.append((island_row+1,island_col))
                        if island_col!=0 and grid[island_row][island_col-1]=="1":
                            queue.append((island_row,island_col-1))
                        if island_row!=0 and grid[island_row-1][island_col]=="1":
                            queue.append((island_row-1,island_col))
        return number_of_islands