

#matrix= [[12,4,0,9],[10,5,6,1],[0,7,5,9],[3,5,8,0]]

#print matrix
#for i in range(4):
    #for j in range(4):
     #print(matrix[i][j] ,end="\t   ")

    #print()
    

#print()

#double
#for i in range(4):
    #for j in range(4):
    #print(matrix[i][j] * 2 ,end="\t  ")

    #print()


#print()


#exchange

#for j in range(4):
    #for i in range(4):
    # print(matrix[i][j] ,end="\t   ")

    #print()


matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7,8], [9, 10], [11,12]]
matrix3 = [[0,0], [0, 0]]

#print(matrix)

def print_matrix(matrix):
    print(" -\t-")
    for i in range(len(matrix)):
        print("|", end=" ")
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print(" |", end="  ")
        print()
    print(" -\t-")

def multiply_matrix(mat_1, mat_2):
    for i in range(len(mat_1)):
        for j in range(len(mat_2[0])):
            for k in range(len(mat_2)):
                matrix3[i][j] += mat_1[i][k] * mat_2[k][i]
            print_matrix(matrix3)

print_matrix(matrix1)
print_matrix(matrix2)

multiply_matrix(matrix1, matrix2)
print_matrix(matrix3)





          


    





