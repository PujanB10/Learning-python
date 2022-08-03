def print_sudoku(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                board[i][j]="_"
            m=f"{board[i][j]} "
            if (j+1)%3==0:
                m+=" "
            print(m,end="")
        print("")
        if (i+1)%3==0:
            print("")

def copy_and_add(original_board,row_change,column,digit):
    new_board=[]
    for row in original_board:
        new_board.append(row[:])
    new_board[row_change][column]=digit
    return new_board



if __name__ == "__main__":
    sudoku  = [
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]
              ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
