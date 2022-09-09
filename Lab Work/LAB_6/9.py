class Bill():
    def __init__(self,name,tableno, order):
        self.name = name
        self.tableno= tableno
        self.order = order

    def orderData(self):      
        orderList = self.order.split(",")
        orderQtyLst = []

        for item in orderList:
            orderQtyLst.append(item.split("x"))
        return(orderQtyLst)


bill1 = Bill("vishnu",5,"Item1x1,Item2x3,Item3x1")
print(bill1.orderData())

class RestaurantBill(Bill):
    def __init__(self,name,tableno, order,orderData, prices):
        super().__init__(name, tableno, order)
        self.name = name
        self.tableno = tableno
        self.order = order
        self.orderData = orderData

        price_list = []
        orderPriceLst = prices.split(",")

        for item in orderPriceLst:
            price_list.append(item.split("-"))

        self.price_list = price_list
    
    def calculatePrice(self):
        orderQuantityPrice = []
        totalPrice = 0
        for order in self.orderData:
             for price in self.price_list:
                if order[0] == price[0]:
                    orderQuantityPrice.append([order[0],order[1], price[1]])
                    totalPrice += int(order[1]) * int(price[1])
                    break
        self.orderQuantityPrice = orderQuantityPrice

        return(totalPrice)

    def generateBill(self): 
        billData = []
        print("-----BILL-----")
        for order in self.orderQuantityPrice:
            print(f"{order[0]} --- {order[1]}Qty * {order[2]}Rs = {int(order[1])*int(order[2])}Rs" )
        print("Total = ", self.calculatePrice())
        print("------------")
            

pricesList ="Item1-100,Item2-70,Item3-250"
rest1 = RestaurantBill("vishnu",5,"Item1x1,Item2x3,Item3x1",bill1.orderData(),pricesList)
print(rest1.calculatePrice())
rest1.generateBill()