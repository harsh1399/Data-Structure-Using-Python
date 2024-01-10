'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

'''


from typing import List
class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_time = 0
        max_time = 0
        queue = list()
        for row_index in range(len(grid)):
            for col_index in range(len(grid[row_index])):
                if grid[row_index][col_index] == 2:
                    queue.append(((row_index,col_index),0))
        while len(queue)!=0:
            count = 0
            index,time = queue.pop(0)
            row,col = index
            if time > max_time:
                max_time = time
            if col!=len(grid[0])-1 and grid[row][col+1]==1:
                queue.append(((row,col+1),time+1))
                grid[row][col+1] = -1
            if col!=0 and grid[row][col-1]==1:
                queue.append(((row,col-1),time+1))
                grid[row][col-1] = -1
            if row!=len(grid)-1 and grid[row+1][col] == 1:
                queue.append(((row+1,col),time+1))
                grid[row+1][col] = -1
            if row!=0 and grid[row-1][col] == 1:
                queue.append(((row-1,col),time+1))
                grid[row-1][col] = -1
        for row in grid:
            for val in row:
                if val == 1:
                    return -1
        return max_time