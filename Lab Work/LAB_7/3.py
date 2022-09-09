f1 = open('customerNames.txt','r')
f2 = open('tableNumbers.txt','r')
f3 = open('orderDetails.txt','r')
f4 = open('priceList.txt','r')

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



    billFile = open('Billfile.txt',"a")
    # print(billFile.read())
    billFile.write("___BILL___\n")
    billFile.write(f"Customer Name:{names[i].strip()}\n")
    for item in bill:
        print(bill[item])
        itemDetail = bill[item]
        # print(itemDetail["qty"])
        billFile.write(f"{item}:{itemDetail['qty']} * {itemDetail['price']} = {itemDetail['qty'] * itemDetail['price']}\n")

    billFile.write(f"Total:{totalPrice}\n")
    billFile.write("___________\n")
        
    



