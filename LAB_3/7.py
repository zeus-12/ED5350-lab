a = [[1,2],[3,4]]
# 1 2
# 3 4

b = [[5,6],[7,8]]
# 5 6
# 7 8

# interchange i-th row of a with i-th row of b
def interchangeRows(a,b,i):
    a_removed = a.pop(i)
    b_removed = b.pop(i)
    b.insert(i,a_removed)
    a.insert(i, b_removed)
    return(a,b)  

# interchange i-th column of a with i-th column of b
def interchangeCols(a,b,i):
    a_cols = list(zip(*a)) 
    b_cols = list(zip(*b)) 
    a_cols[i],b_cols[i]= b_cols[i],a_cols[i]
    a_rows = list(zip(*a_cols)) 
    b_rows = list(zip(*b_cols))
    return (a_rows,b_rows)

a,b = interchangeRows(a,b,1)
a,b = interchangeCols(a,b,1)
print(a,b)
