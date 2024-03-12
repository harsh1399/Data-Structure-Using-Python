'''
Consider a matrix with rows and columns, where each cell contains either a ‘0’ or a ‘1’ and any cell containing a 1 is called a filled cell.
Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally.
If one or more filled cells are also connected, they form a region. find the length of the largest region
'''

def largestRegion(M):
    maxRegionArea = 0
    for row_ind in range(len(M)):
        for col_ind in range(len(M[0])):
            if M[row_ind][col_ind] == 1:
                regionArea = 1
                queue = list()
                queue.append((row_ind, col_ind))
                M[row_ind][col_ind] = -1
                while len(queue) != 0:
                    r, c = queue.pop(0)
                    if r != 0 and M[r - 1][c] == 1:
                        queue.append((r - 1, c))
                        regionArea += 1
                        M[r-1][c] = -1
                    if c != 0 and M[r][c - 1] == 1:
                        queue.append((r, c - 1))
                        regionArea += 1
                        M[r][c-1] = -1
                    if r != len(M) - 1 and M[r + 1][c] == 1:
                        queue.append((r + 1, c))
                        regionArea += 1
                        M[r+1][c] = -1
                    if c != len(M[0]) - 1 and M[r][c + 1] == 1:
                        queue.append((r, c + 1))
                        regionArea += 1
                        M[r][c+1] = -1
                    if r != 0 and c != 0 and M[r - 1][c - 1] == 1:
                        queue.append((r - 1, c - 1))
                        regionArea += 1
                        M[r - 1][c-1] = -1
                    if r != len(M) - 1 and c != 0 and M[r + 1][c - 1] == 1:
                        queue.append((r + 1, c - 1))
                        regionArea += 1
                        M[r + 1][c-1] = -1
                    if r != len(M) - 1 and c != len(M[0]) - 1 and M[r + 1][c + 1] == 1:
                        queue.append((r + 1, c + 1))
                        regionArea += 1
                        M[r + 1][c+1] = -1
                    if r != 0 and c != len(M[0]) - 1 and M[r - 1][c + 1] == 1:
                        queue.append((r - 1, c + 1))
                        regionArea += 1
                        M[r - 1][c + 1] = -1
                if regionArea > maxRegionArea:
                    maxRegionArea = regionArea

    return maxRegionArea


ROW = 4
COL = 5

M = [[1, 1, 1, 1, 1],
     [1, 0, 0, 0, 0],
     [1, 0, 1, 0, 0],
     [1, 1, 1, 1, 1]]

print(largestRegion(M))