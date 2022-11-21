import pygame

M = 9


def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()


def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def Suduko(grid, row, col):
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1):

        if solve(grid, row, col, num):

            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
      [0, 1, 0, 0, 0, 4, 0, 0, 0],
      [4, 0, 7, 0, 0, 0, 2, 0, 8],
      [0, 0, 5, 2, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 9, 8, 1, 0, 0],
      [0, 4, 0, 0, 0, 3, 0, 0, 0],
      [0, 0, 0, 3, 6, 0, 0, 7, 2],
      [0, 7, 0, 0, 0, 0, 0, 0, 3],
      [9, 0, 3, 0, 0, 0, 6, 0, 4]]

if (Suduko(grid, 0, 0)):
    puzzle(grid)
else:
    print("Solution does not exist:(")

pygame.init()
surface = pygame.display.set_mode((475, 475))
background_colour = (255,255,255)
color = (0, 0, 0)
pygame.display.set_caption('Sudoku Solver')
surface.fill(background_colour)
xnum = 0
ynum = 0
x = 30
y = 30
while ynum < 9:
    while xnum < 9:
        pygame.draw.rect(surface, color, pygame.Rect(x, y, 40, 40), 2)
        x += 40
        xnum += 1
    xnum = 0
    x = 30
    y += 40
    ynum += 1


pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


