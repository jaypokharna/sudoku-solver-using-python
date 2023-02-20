import numpy as np

sudoku = [[0, 0, 0, 0, 0, 0, 2, 0, 0],
          [0,8,0,0,0,7,0,9,0],
          [6,0,2,0,0,0,5,0,0],
          [0,7,0,0,6,0,0,0,0],
          [0,0,0,9,0,1,0,0,0],
          [0,0,0,0,2,0,0,4,0],
          [0,0,5,0,0,0,6,0,3],
          [0,9,0,4,0,0,0,7,0],
          [0,0,6,0,0,0,0,0,0]]

print("Original Sudoku \n\n", np.matrix(sudoku), "\n\n Solution\n")


def solution (row,col,num):
        global sudoku

        # To check if the number is present in given row
        for i in range(0,9):
                if sudoku[row][i] == num:
                        return False

        # To check if the number is present in given row
        for i in range(0,9):
                if sudoku[i][col] == num:
                        return False

        # To check if the number is present in given square
        x0 = (col // 3) *3
        y0 = (row // 3) * 3

        for i in range(0,3):
                for j in range(0,3):
                        if sudoku[y0 + i][x0 + j] == num:
                                return False

        return True

def solve():
        global sudoku
        for row in range(0,9):
                for col in range(0,9):
                        if sudoku[row][col] == 0:
                                for num in range(1,10):
                                        if(solution(row,col,num)): #will work if solution method return true
                                                sudoku[row][col] = num
                                                solve()
                                                sudoku[row][col] = 0

                                return
        print(np.matrix(sudoku))
        input('\nFor more possible solutions(If possible) hit enter - ')
solve()