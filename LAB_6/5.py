import random


class Base1:
    def __init__(self, m, n):
        self.mat = [[random.randint(1, 9) for i in range(n)] for j in range(m)]

    def __add__(self, m):
        if len(self.mat) != len(m.mat) or len(self.mat[0]) != len(m.mat[0]):
            return "Error"
        res = [[0 for i in range(len(self.mat[0]))] for j in range(len(self.mat))]
        for i in range(len(m.mat)):
            for j in range(len(m.mat[0])):
                res[i][j] = self.mat[i][j] + m.mat[i][j]
        return res

    def __sub__(self, m):
        if len(self.mat) != len(m.mat) or len(self.mat[0]) != len(m.mat[0]):
            return "Error"
        res = [[0 for i in range(len(self.mat[0]))] for j in range(len(self.mat))]
        for i in range(len(m.mat)):
            for j in range(len(m.mat[0])):
                res[i][j] = self.mat[i][j] - m.mat[i][j]
        return res

    def __mul__(self, m):
        if len(self.mat[0]) != len(m.mat):
            return "Error"

        res = [[0 for i in range(len(m.mat[0]))] for j in range(len(self.mat))]
        for i in range(len(self.mat)):
            for j in range(len(m.mat[0])):
                for k in range(len(m.mat)):
                    res[i][j] += self.mat[i][k] * m.mat[k][j]
        return res


class Base2:
    def __init__(self, m, n):
        self.mat = [[random.randint(1, 9) for i in range(n)] for j in range(m)]

    def element_mul(self, m):
        if len(self.mat) != len(m.mat) or len(self.mat[0]) != len(m.mat[0]):
            return "Error"
        res = [[0 for i in range(len(self.mat[0]))] for j in range(len(self.mat))]
        for i in range(len(m.mat)):
            for j in range(len(m.mat[0])):
                res[i][j] = self.mat[i][j] * m.mat[i][j]
        return res

    def scalar(self, k):
        return list(map(lambda x: [k*i for i in x], self.mat))


class Base12(Base1, Base2):
    def __init__(self, m, n):
        super().__init__(m, n)


a = Base12(4, 4)
b = Base12(4, 4)

print("Addition :", a+b)
print("Subtraction :", a-b)
print("Multiplication :", a*b)
print("Element by Element Multiplication :", a.element_mul(b))
print("Scalar Multiplication :", a.scalar(2))