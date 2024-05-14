'''
leetcode 1219
'''
from typing import List
import copy

class Solution:
    def dfs(self,grid,i,j,gold,maxval):
        current_val = grid[i][j]
        # print(current_val)
        gold += current_val
        if gold > maxval:
            maxval = gold
        grid[i][j] = 0
        if i!=0 and grid[i-1][j]!=0:
            a = self.dfs(grid,i-1,j,gold,maxval)
            if a > maxval:
                maxval = a
        if i!=len(grid)-1 and grid[i+1][j]!=0:
            b = self.dfs(grid,i+1,j,gold,maxval)
            if b > maxval:
                maxval = b
        if j!=0 and grid[i][j-1]!=0:
            c = self.dfs(grid,i,j-1,gold,maxval)
            if c > maxval:
                maxval = c
        if j!=len(grid[0])-1 and grid[i][j+1]!=0:
            d = self.dfs(grid,i,j+1,gold,maxval)
            if d > maxval:
                maxval = d
        # print("dead end--backtracking")
        grid[i][j] = current_val
        return maxval

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxGold = 0
        maxVal = 0
        gold = 0
        for row_ind in range(len(grid)):
            for col_ind in range(len(grid[0])):
                if grid[row_ind][col_ind]!=0:
                    # print(f"startig:{grid[row_ind][col_ind]}")
                    val = self.dfs(copy.deepcopy(grid),row_ind,col_ind,gold,maxVal)
                    # print(f"val:{val}")
                    if val > maxGold:
                        maxGold = val

        return maxGold
