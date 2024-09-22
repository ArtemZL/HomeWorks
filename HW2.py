def func(points):
    x0, y0 = points[0]
    x1, y1 = points[1]
    if len(points) < 2:
        return True

    dx, dy = x1 - x0, y1 - y0

    for i in range(2, len(points)):
        x, y = points[i]
        if(y - y0) * dx != (x - x0) * dy:
            return False
    return True

points = [[1,2], [2,3], [3,4]]
print(func(points))


def sort_diagonal(mat):
    m = len(mat)
    n = len(mat[0])

    for i in range(m):
        diag = []
        row, col = i, 0
        while row < m and col < n:
            diag.append(mat[row][col])
            row += 1
            col += 1

        diag.sort()
        row, col = i, 0
        for k in range(len(diag)):
            mat[row][col] = diag[k]
            row += 1
            col += 1

    for j in range(1, n):
        diag = []
        row, col = 0, j
        while row < m and col < n:
            diag.append(mat[row][col])
            row += 1
            col += 1

        diag.sort()
        row, col = 0, j
        for k in range(len(diag)):
            mat[row][col] = diag[k]
            row += 1
            col += 1

    return mat

matrix = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
sorted_matrix = sort_diagonal(matrix)
for row in sorted_matrix:
    print(row)

def attack(queens, king):
    attacking_queens = []
    for queen in queens:
        if (queen[0] == king[0] or
            queen[1] == king[1] or
            abs(queen[0] - king[0]) == abs(queen[1] - king[1])):
            attacking_queens.append(queen)
    return attacking_queens
queens = [(0, 1), (2, 3), (5, 4), (7, 7)]
king = (0, 7)
attacking_queens = attack(queens, king)
print("Ферзі, які атакують короля:", attacking_queens)


def dfs_recursive(grid, x, y, visited):
    n = len(grid)
    m = len(grid[0])

    if (x < 0 or x >= n or y < 0 or y >= m
            or visited[x][y] or grid[x][y] == 0):
        return 0
    visited[x][y] = True
    size = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        size += dfs_recursive(grid, x + dx, y + dy, visited)

    return size

def largest_group_recursive(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    largest_size = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                group_size = dfs_recursive(grid, i, j, visited)
                largest_size = max(largest_size, group_size)
    return largest_size

grid = [
    [0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0]
]
largest_size = largest_group_recursive(grid)
print("Найбільша група одиниць має розмір:", largest_size)



