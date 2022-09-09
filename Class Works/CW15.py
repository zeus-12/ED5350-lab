#File Modes
#both reading and writing are in the form of strings
#f = open('messages.txt','w') #Opens a file for writing
#f = open('messages.txt','r') #Opens file for reading
msg1 = 'This is message 1\n'
msg2 = 'This is message 2\n'
msg3 = 'This is message 3\n'

f = open('messages.txt','w')
f.write(msg1)
f.write(msg2)
f.write(msg3)
f.close()

f = open('messages.txt','r')
data = f.read()
print(data)
print(data[0])
print(type(data))
f.close()

tup = ('Ram', 23, 1456)
lst = [1,2,3]
dct = {'name': 'vishnu', 'ROLL':12345}
f = open('messages.txt','w')
f.write(str(tup))
f.write(str(lst))
f.write(str(dct))
f.close()

f = open('messages.txt','r')
data = f.read()
print(data)

f.seek(0)
data = f.read(10)
print(data)
print(type(data))
f.seek(0)
data = f.readline()
print(data)
f.seek(0)
data = f.readlines()
f.close()

f = open('numbers.txt','w+')
f.write(str(1234))
f.write(str(123.45))
f.seek(0)
#a = int(f.readline())
b = float(f.readline())
#print(a,b)
print(b)

import os
print(os.name)
print(os.getcwd()) #will get you the current working directory
print(os.listdir('.'))
print(os.listdir('..'))

if os.path.exists('TestDir'):
    print('TestDir exists')
else:
    os.mkdir('TestDir')

os.chdir('TestDir')
print(os.getcwd())

f = open('myfile','w')
f.write('This is a created file')
f.close()
stats = os.stat('myfile')
print(stats.st_size)

import csv

with open('test_csv1.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Header names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and handles {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

with open('test_data_csv1.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    x = []
    y = []
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} is x-data and {row[1]} is y-data.')
            x.append(int(row[0]))
            y.append(int(row[1]))
            line_count += 1
    print(f'Processed {line_count} lines.')
    print(x, y)

