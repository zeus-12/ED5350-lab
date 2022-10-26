import os
dir = os.path.dirname(__file__)
header = 'Students: marks'
data = ["Vishnu: 20","Pranoy: 50","Albin: 80","Thazeel: 50", "Nihad: 70"]

fileName = os.path.join(dir,'marksList.txt')

f = open(fileName,'w')

f.write(header)
f.write('\n')

for mark in data:
    f.write(mark)
    f.write('\n')
f.close()

