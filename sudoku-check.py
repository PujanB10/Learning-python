
def row_correct(board,in_row):
    numbers=[]
    for element in board[in_row]:
        if element>0 and element in numbers:
            return False
        numbers.append(element)
    return True

def column_correct(board,column):
    numbers=[]
    for row in board:
        if row[column]>0 and row[column] in numbers:
            return False
        numbers.append(row[column])
    return True 

def block_correct(board,row,column):
    numbers=[]
    for i in range(row,row+3):
        for j in range(column,column+3):
            if board[i][j]>0 and board[i][j] in numbers:
                return False
            numbers.append(board[i][j])
    return True    



def sudoku_grid_correct(sudoku):
    for i in range(0,7,3):
        for j in range(0,7,3):
            is_row_correct=row_correct(sudoku,i)
            is_column_correct=column_correct(sudoku,j)
            is_block_correct=block_correct(sudoku,i,j)
            if not (is_row_correct or is_column_correct or is_block_correct):
                return False
    return True
                
    

if __name__ == "__main__":
    sudoku1 = [
              [2, 6, 7, 8, 3, 9, 5, 0, 4],
              [9, 0, 3, 5, 1, 0, 6, 0, 0],
              [0, 5, 1, 6, 0, 0, 8, 3, 9],
              [5, 1, 9, 0, 4, 6, 3, 2, 8],
              [8, 0, 2, 1, 0, 5, 7, 0, 6],
              [6, 7, 4, 3, 2, 0, 0, 0, 5],
              [0, 0, 0, 4, 5, 7, 2, 6, 3],
              [3, 2, 0, 0, 8, 0, 0, 5, 7],
              [7, 4, 5, 0, 0, 3, 9, 0, 1]
              ]

  

    print(sudoku_grid_correct(sudoku1))
