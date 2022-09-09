import csv  

header = ['Students', 'marks']
data = [['Vishnu',20],['Pranoy',50],['Albin',80],['Thazeel',50], ['Nihad',70]]

with open('markList.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    for dataRow in data:
        writer.writerow(dataRow)
