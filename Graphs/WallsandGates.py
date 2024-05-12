'''
You are given a m x n 2D grid initialized with these three possible values. -1 - A wall or an obstacle. 0 - A gate.
INF - Infinity means an empty room Fill each empty room with the distance to its nearest gate.
'''

class Solution():
    def wallsAndGates(self, rooms):
        # Write your code here
        queue = list()
        for row_index in range(len(rooms)):
            for col_index in range(len(rooms[0])):
                if rooms[row_index][col_index] == 0:
                    queue.append((row_index, col_index, 0))
        while len(queue) != 0:
            row_index, col_index, step = queue.pop(0)
            if row_index != 0 and rooms[row_index - 1][col_index] == float("Inf"):
                rooms[row_index - 1][col_index] = step + 1
                queue.append((row_index - 1, col_index, step + 1))
            if row_index != len(rooms) - 1 and rooms[row_index + 1][col_index] == float("Inf"):
                rooms[row_index + 1][col_index] = step + 1
                queue.append((row_index + 1, col_index, step + 1))
            if col_index != 0 and rooms[row_index][col_index - 1] == float("Inf"):
                rooms[row_index][col_index - 1] = step + 1
                queue.append((row_index, col_index - 1, step + 1))
            if col_index != len(rooms[0]) - 1 and rooms[row_index][col_index + 1] == float("Inf"):
                rooms[row_index][col_index + 1] = step + 1
                queue.append((row_index, col_index + 1, step + 1))
        print(rooms)
        return None


rooms = [
    [float("Inf"), -1, 0, float("Inf")],
    [float("Inf"), float("Inf"), float("Inf"), -1],
    [float("Inf"), -1, float("Inf"), -1],
    [0, -1, float("Inf"), float("Inf")]
]

test = Solution()
test.wallsAndGates(rooms)
