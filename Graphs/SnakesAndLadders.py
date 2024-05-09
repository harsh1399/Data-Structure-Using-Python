## LEETCODE - 909
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        row = len(board)
        col = len(board[0])
        visited = [0] * (row * col)
        board.reverse()
        # print(len(visited))
        queue = list()
        queue.append((1, 0))
        visited[0] = 1
        while len(queue) != 0:
            current, dice_times = queue.pop(0)
            # print(f"Current number:{current}")
            if current == row * col:
                return dice_times
            for i in range(1, 7):
                if current + i <= row * col:
                    row_no = (current + i - 1) // row
                    col_no = ((current + i) - 1) % col
                    if row_no % 2 != 0:
                        col_no = col - col_no - 1

                    # print(f"current+i:{current+i} row:{row_no}, col:{col_no}")
                    if board[row_no][col_no] != -1:
                        if visited[board[row_no][col_no] - 1] != 1:
                            # print(f"adding {board[row_no][col_no]} in the queue")
                            queue.append((board[row_no][col_no], dice_times + 1))
                            visited[board[row_no][col_no] - 1] = 1

                    else:
                        if visited[current + i - 1] != 1:
                            # print(f"adding {current+i} in the queue")
                            queue.append((current + i, dice_times + 1))
                            visited[current + i - 1] = 1
                            # print(visited)
                    # print(f"queue: {queue}")
        return -1