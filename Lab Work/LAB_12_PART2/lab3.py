import numpy as np
from sklearn.svm import SVC
from sklearn.decomposition import PCA


X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])

model = SVC()
model.fit(X, y)
print(model.predict([[-0.8, -1]]))

Model = PCA(n_components=2)

X_new = Model.fit_transform(X)
print(X_new)

