import pandas as pd

res = []
for i in range(5):
    name = input("Name : ")
    marks = input("Marks : ")
    res.append([name, marks])

w = pd.DataFrame(res, columns=['Student', 'Marks'])
w.to_csv('marklist.csv', index=False)


