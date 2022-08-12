def transpose(mat):
    for row_index in range(3):
        for col_index in range(3):
            mat[row_index][col_index], mat[col_index][row_index] = mat[col_index][row_index],mat[row_index][col_index] 
        
    return mat





def addition(mat_1,mat_2):
    result=[]
    for row_index in range(3):
        cur_row = [0,0,0]
        for col_index in range(3):
            cur_row[col_index] = mat_1[row_index][col_index] + mat_2[row_index][col_index]
        result.append(tuple(cur_row))

    return(result)

def subtraction(mat_1,mat_2):
    result=[]
    for row_index in range(3):
        cur_row = [0,0,0]
        for col_index in range(3):
            cur_row[col_index] = mat_1[row_index][col_index] - mat_2[row_index][col_index]
        result.append(tuple(cur_row))

    return(result)

# matrix 1
a_row_1 = [1,2,3]
a_row_2 = [7,8,9]
a_row_3 = [4,5,6]

# matrix 2
b_row_1 = [3,5,7]
b_row_2 = [9,7,5]
b_row_3 = [1,5,9]

matrix_1 = list(zip(a_row_1,a_row_2,a_row_3))
print(matrix_1)

matrix_2 = list(zip(b_row_1,b_row_2,b_row_3))
print(matrix_2)


sum = addition(matrix_1,matrix_2)
print("Sum is", sum)

diff = subtraction(matrix_1,matrix_2)
print("Difference is ",diff)


transpose_1 = transpose(matrix_1)
print(f"{transpose_1} is the transpose of {matrix_1}")

# mat1 = ([1,2,3,4],[5,6,7,8])
# print(mat1)
# print(*mat1)

# ite = zip(*mat1)
# print(*ite)

# lst = list(ite)
# print(lst)   