size = 9

def isValid(grid, row, col, num):

  #check for repeats in same row (horizontal)
  for i in range(9):
    if grid[row][i] == num:
      return False

  #check for repeats in column (vertical)
  for j in range(9):
    if grid[j][col] == num:
      return False

  #check for repeats in the same box
  r = row - row%3
  c = col - col%3
  for i in range(3):
    for j in range(3):
      if grid[r+i][c+j]:
        return False
  return True

