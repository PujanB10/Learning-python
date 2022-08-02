def row_correct(board,in_row):
    numbers=[]
    for element in board[in_row]:
        if element>0 and element in numbers:
            return False
        numbers.append(element)
    return True

if __name__ == "__main__":
    sudoku = [
            [9, 0, 0, 0, 8, 0, 3, 0, 0],
            [2, 0, 0, 2, 5, 0, 7, 0, 0],
            [0, 2, 0, 3, 0, 0, 0, 0, 4],
            [2, 9, 4, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 7, 3, 0, 5, 6, 0],
            [7, 0, 5, 0, 6, 0, 4, 0, 0],
            [0, 0, 7, 8, 0, 3, 9, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 2]
            ]
    print(row_correct(sudoku, 1))
