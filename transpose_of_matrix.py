def transpose(my_matrix):
    j=0
    for i in range(len(my_matrix)):
        for j in range(i,len(my_matrix)):
            temp=my_matrix[i][j]
            my_matrix[i][j]=my_matrix[j][i]
            my_matrix[j][i]=temp


if __name__ == "__main__":
    matrix=[[1,2,3,4],[4,5,6,7],[7,8,9,8],[1,2,3,4]]
    transpose(matrix)
    print(matrix)
