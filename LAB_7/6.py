import numpy as np

a = np.array([[4, 5, 6], [7, 8, 9],[1, 2, 3]])
b = np.array([[6, 5, 4], [3, 2, 1],[9, 8, 7]])

print("Dot Product :", np.dot(a, b))
print("Transpose :", np.transpose(a))
print("Trace :", np.trace(a))
print("Rank :", np.linalg.matrix_rank(a))
print("Determinant :", np.linalg.det(a))

x, y = np.linalg.eig(a)


print("Eigenvalues :", x)
print("Eigenvectors :", y)
