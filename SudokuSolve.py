import random    

def parse_data(filename, n):
    file = open(filename,"r")
    for i in range(n+1):
        lines = file.readline()
    file.close()
    line = lines.split("\n")[:1]
    line = line[0]
    retlist = []
    retlist = line.split(",")
    return retlist


#TEST THIS, NEED TO WRITE THIS IN IN THE MAIN CODE FLOW THING

def gridparse(string):
    num = 0
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(9):
        for j in range(9):
            grid[i][j] = string[num]
            num += 1
    print(num)
    return grid




#This algorithm doesn't work PROOF that i was right
def randomBoard():
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(9):
        for j in range(9):
            print(grid)
            num = 1
            count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            
            while (not isValid(grid, i, j, num)):
        
            #when count = a list of ones, that means all possibilites have been tried and none work
                if count == [1, 1, 1, 1, 1, 1, 1, 1, 1]:
                    return grid
        
                num = random.randint(1, 9)
                print(not isValid(grid, i, j, num))
                print(not count == [1, 1, 1, 1, 1, 1, 1, 1, 1])
                count[num-1] = 1
      
          
            grid[i][j] = num
      
    return grid

#--------------------------------------------------------------

def printBoard(grid):
  print("------------------------------")
  for i in range(9):
    string = ""
    if i == 3 or i == 6 or i == 9:
      print("------------------------------")
    for j in range(9):
      string += " "+str(grid[i][j]) + " "
      if j == 2 or j == 5 or j == 8:
        string += "|"
    
    print(string)


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
            if grid[r+i][c+j] == num:
                return False
    return True



def solve(grid, row, col):
    #basecases
    #end of the board, this spot is one after the end of the board
    if (row == 8 and col == 9):
        return True
  
    #end of row, not last column
    if col == 9:
        col = 0
        row += 1
  
    #filled box: skips to next
    if grid[row][col] != 0:
        return solve(grid, row, col+1)
  
    #iterate through 1-9, check if valid then recurse
    for n in range(1, 10, 1):
        if isValid(grid, row, col, n):
            grid[row][col] = n
            if solve(grid, row, col+1):
                return True
        grid[row][col] = 0
    return False
      
      
grid = [[8, 0, 1, 9, 0, 0, 0, 4, 0], 
        [0, 4, 0, 8, 5, 1, 0, 2, 0], 
        [0, 5, 6, 0, 7, 0, 0, 9, 1], 
        [0, 3, 0, 0, 0, 5, 0, 7, 0], 
        [0, 0, 0, 0, 3, 0, 1, 0, 0],
        [7, 6, 0, 2, 0, 0, 5, 0, 8],
        [4, 2, 0, 0, 6, 8, 9, 1, 0],
        [0, 0, 0, 3, 0, 0, 6, 8, 7],
        [0, 0, 3, 1, 0, 0, 2, 5, 0],]
      
grid2 = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5,  2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
      
grid3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def main():
    print('Sudoku Solver\n')
    
    #sudoku CSV
    filename = "sudoku.csv"
    sudokus = []
    sudokus.append(parse_data(filename, 1))
    sudokus.append(parse_data(filename, 2))
    
    
    
    if solve(grid, 0, 0):
        solve(grid, 0, 0)
        printBoard(grid)
    else:
        print("No Solution")

main()
    









