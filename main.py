from tabulate import tabulate
import sys
import csv

def is_empty(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return [row, col]

    return None

def is_safe(board, x, y):
    number = board[x][y]

    #check row
    for col in range(len(board)):
        if board[x][col] == number and col != y:
            return False

    #check col
    for row in range(len(board)):
        if board[row][y] == number and row != x:
            return False

    #check box
    startRow = x - (x % 3)
    startCol = y - (y % 3)

    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == number and (i + startRow != x or j + startCol != y):
                return False


    return True

def solve(board):
    empty = is_empty(board)

    if empty == None:
        return True

    x, y = empty[0], empty[1]

    for i in range(1, 10):
        board[x][y] = i
        if is_safe(board, x, y):

            if solve(board):
                return True
        board[x][y] = 0

    return False


def main():

    if len(sys.argv) != 2:
        print("Wrong amount of files")
        sys.exit(-1)
    else:
        fileType =  sys.argv[1][-4:]
        if fileType != ".csv":
            print("Not a csv file")
            sys.exit(-1)
        else:
            try:
                board = []
                with open(sys.argv[1]) as file:
                    reader = csv.reader(file)

                    for row in reader:
                        nums = list(map(int, row))
                        board.append(nums)
            except:
                print("File does not exist")
                sys.exit(-1)

    solve(board)


    print(tabulate(board, tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()
