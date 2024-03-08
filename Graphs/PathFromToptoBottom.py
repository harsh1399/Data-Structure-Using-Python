def findValidPath(mat, i, j, grid):
    if i == len(mat) - 1 and j == len(mat[0]) - 1:
        grid[i][j] = 1
        return 1
    grid[i][j] = 1
    mat[i][j] = 0
    if not i == 0 and mat[i - 1][j] == 1:
        if findValidPath(mat, i - 1, j, grid) == 1:
            return 1
    if not i == len(mat) - 1 and mat[i + 1][j] == 1:
        if findValidPath(mat, i + 1, j, grid) == 1:
            return 1
    if not j == 0 and mat[i][j - 1] == 1:
        if findValidPath(mat, i, j - 1, grid) == 1:
            return 1
    if not j == len(mat[0]) and mat[i][j + 1] == 1:
        if findValidPath(mat, i, j + 1, grid) == 1:
            return 1
    grid[i][j] = 0
    return 0


def findPaths(mat, i, j):
    # write your code here
    first_row = [0] * len(mat[0])
    # grid = [first_row.copy()] * len(mat)
    grid = [ [0]*len(mat[0]) for j in range(len(mat))]
    pathPossible = findValidPath(mat, i, j, grid)
    if pathPossible == 1:
        print(grid)
    else:
        print("path not possible")
    return grid


if __name__ == '__main__':
    mat = [
        [1, 0, 0],
        [1, 1, 1],
        [1, 0, 1]
    ]

    # start from (0, 0) cell
    x = y = 0

    findPaths(mat, x, y)