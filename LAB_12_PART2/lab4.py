import numpy as np

def pca(X, n):
    C = X - np.mean(X, axis=0)
    V = np.cov(C, rowvar=False)

    e_values, e_vectors = np.linalg.eig(V)
    index_no = np.argsort(e_values)[::-1]

    e_values = e_values[index_no]
    e_vectors = e_vectors[:, index_no]
    e_vectors = e_vectors[:, :n]

    res = np.dot(e_vectors.transpose(), C.transpose()).transpose()
    return res
    
    
X = np.array([[1, 2, 3], [2, 4, 3], [6, 3, 4], [1, 7, 3]])
num = 2

X_new = pca(X, num)
print(X_new)


    
# Yes, It's the same result