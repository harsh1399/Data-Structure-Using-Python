'''You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.'''


from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for row_index in range(len(grid)):
            for col_index in range(len(grid[row_index])):
                if grid[row_index][col_index] == 1:
                    area = 0
                    queue = []
                    queue.append((row_index,col_index))
                    grid[row_index][col_index] = 0
                    while len(queue)!=0:
                        island_row,island_col = queue.pop()
                        area += 1
                        if island_col!= len(grid[row_index])-1 and grid[island_row][island_col+1]==1:
                            queue.append((island_row,island_col+1))
                            grid[island_row][island_col+1] = 0
                        if island_row!=len(grid)-1 and grid[island_row+1][island_col]==1:
                            queue.append((island_row+1,island_col))
                            grid[island_row+1][island_col] = 0
                        if island_col!=0 and grid[island_row][island_col-1]==1:
                            queue.append((island_row,island_col-1))
                            grid[island_row][island_col-1] = 0
                        if island_row!=0 and grid[island_row-1][island_col]==1:
                            queue.append((island_row-1,island_col))
                            grid[island_row-1][island_col] = 0
                    if area > max_area:
                        max_area = area
        return max_area