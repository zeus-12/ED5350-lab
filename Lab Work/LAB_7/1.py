header = 'Students: marks'
data = ["Vishnu: 20","Pranoy: 50","Albin: 80","Thazeel: 50", "Nihad: 70"]


f = open('marksList.txt','w')

f.write(header)
f.write('\n')

for mark in data:
    f.write(mark)
    f.write('\n')
f.close()