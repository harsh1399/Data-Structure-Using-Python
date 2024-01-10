'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''


from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        not_flip = []
        visited = [[0 ] *len(board[0]) for i in range(len(board))]
        queue = list()
        for row_index in range(len(board)):
            for col_index in [0 ,len(board[0] ) -1]:
                if board[row_index][col_index] == "O":
                    queue.append((row_index ,col_index))
                    visited[row_index][col_index] = 1
        for col_index in range(len(board[0])):
            for row_index in [0 ,len(board ) -1]:
                if board[row_index][col_index] == "O" and  visited[row_index][col_index ]!=1:
                    queue.append((row_index ,col_index))
                    visited[row_index][col_index] = 1

        while len(queue )!=0:
            row ,col = queue.pop(0)
            not_flip.append((row ,col))
            if col!=len(board[0] ) -1 and board[row][col +1] == "O" and visited[row][col +1 ]!=1:
                queue.append((row ,col +1))
                visited[row][col +1] = 1
                # not_flip.append((row,col+1))
            if col!=0 and board[row][col -1] == "O" and visited[row][col -1 ]!=1:
                queue.append((row ,col -1))
                visited[row][col -1] = 1
                # not_flip.append((row,col-1))
            if row!= len(board ) -1 and board[row +1][col] == "O" and visited[row +1][col ]!=1:
                queue.append((row +1 ,col))
                visited[row +1][col] = 1
                # not_flip.append((row+1,col))
            if row!=0 and board[row -1][col] == "O" and visited[row -1][col]!=1:
                queue.append((row -1 ,col))
                visited[row -1][col] = 1
                # not_flip.append((row-1,col))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i ,j) not in not_flip and board[i][j ]=="O":
                    board[i][j ] ="X"