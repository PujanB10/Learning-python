def column_correct(board,column):
    numbers=[]
    for row in board:
        if row[column]>0 and row[column] in numbers:
            return False
        numbers.append(row[column])
    return True  
    
if __name__ == "__main__": 
    sudoku =[
            [ 9, 0, 1, 0, 8, 0, 3, 0, 1 ],
            [ 2, 2, 0, 0, 5, 0, 7, 0, 0 ],
            [ 0, 2, 0, 3, 0, 0, 4, 0, 4 ],
            [ 2, 9, 4, 0, 0, 0, 2, 0, 0 ],
            [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
            [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
            [ 0, 0, 7, 8, 0, 3, 9, 8, 6 ],
            [ 3, 0, 1, 0, 0, 0, 0, 0, 1 ],
            [ 3, 0, 0, 0, 2, 0, 2, 0, 1 ],
            ]
    print(column_correct(sudoku, 3))
