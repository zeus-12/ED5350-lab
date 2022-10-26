import os
dir = os.path.dirname(__file__)

fileName1 = os.path.join(dir,'customerNames.txt')
fileName2 = os.path.join(dir,'tableNumbers.txt')
fileName3 = os.path.join(dir,'orderDetails.txt')
fileName4 = os.path.join(dir,'priceList.txt')

f1 = open(fileName1,'r')
f2 = open(fileName2,'r')
f3 = open(fileName3,'r')
f4 = open(fileName4,'r')


names=f1.readlines()
tableno=f2.readlines()
orders=f3.readlines()
prices=f4.read()

for i in range (len(names)):

    ordersWithQty={}

    orderData = orders[i].strip().split(',')
    for item in orderData:
        splitData = item.split('x')
        ordersWithQty[splitData[0]] = splitData[1]

    foodWithPrice={}
    pricesData = prices.split(",")
    for item in pricesData:
        splitPriceData = item.split('-')
        foodWithPrice[splitPriceData[0]] = int(splitPriceData[1])
    
    bill = {}

    totalPrice = 0
    for item in ordersWithQty:
        bill[item] = {"price":foodWithPrice[item],"qty":int(ordersWithQty[item])}
        totalPrice += foodWithPrice[item] * int(ordersWithQty[item])


    billFileLocation = os.path.join(dir,'Billfile.txt')
    billFile = open(billFileLocation,"a")

    billFile.write("___BILL___\n")
    billFile.write(f"Customer Name:{names[i].strip()}\n")
    for item in bill:
        itemDetail = bill[item]
        billFile.write(f"{item}:{itemDetail['qty']} * {itemDetail['price']} = {itemDetail['qty'] * itemDetail['price']}\n")

    billFile.write(f"Total:{totalPrice}\n")
    billFile.write("___________\n")
        
    



