def transposeWZip(mat):
    transpose_lst = list(zip(*mat)) 
    return transpose_lst

def transposeWOZip(mat):
    rows = []
    
    for i in range (3):     
        cur_row = []
        for j in range (3):
            cur_row.append(mat[j][i])    
        rows.append(cur_row)
    return rows

def addition(mat_1,mat_2):
    result=[]
    for row_index in range(3):
        cur_row = [0,0,0]
        for col_index in range(3):
            cur_row[col_index] = mat_1[row_index][col_index] + mat_2[row_index][col_index]
        result.append(cur_row)

    return(result)

def subtraction(mat_1,mat_2):
    result=[]
    for row_index in range(3):
        cur_row = [0,0,0]
        for col_index in range(3):
            cur_row[col_index] = mat_1[row_index][col_index] - mat_2[row_index][col_index]
        result.append(cur_row)

    return(result)

def trace(mat):
    trace = 0
    for i in range (len(mat)):
        trace += mat[i][i]
    return trace



mat1 = ([1,2,3],[7,8,9],[4,5,6])
mat2 = ([3,5,7],[9,7,5],[1,5,9])
# matrix 1
# [1,2,3]
# [7,8,9]
# [4,5,6]

#  matrix 2
# [3,5,7]
# [9,7,5]
# [1,5,9]


sum = addition(mat1,mat2)
print("Sum is", sum)

diff = subtraction(mat1,mat2)
print("Difference is ",diff)


transpose_with_zip = transposeWZip(mat1)
print(f"Transpose w zip is {transpose_with_zip}")


transpose_without_zip = transposeWOZip(mat1)
print(f"Transpose w.o zip is {transpose_without_zip}")

trace_1 = trace(mat1)
print(f"Trace is {trace_1}")