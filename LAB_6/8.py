class Father:
    def __init__(self):
        self.fname = ''
        self.fage = 0
        self.ftalents = []


class Mother:
    def __init__(self):
        self.mname = ''
        self.mage = 0
        self.mtalents = []


class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)


    def getChildDetails(self):
        self.fname = input("Father Name : ")
        self.fage = int(input("Father Age : "))
        res = ''
        while True:
            res = input("Father Talents : ")
            if res == 'x':
                break
            self.ftalents.append(res)
        self.mname = input("Mother Name : ")
        self.mage = int(input("Mother Age : "))
        res = ''
        while True:
            res = input("Mother Talents : ")
            if res == 'x':
                break
            self.mtalents.append(res)
        self.cname = input("Child Name : ")
        self.cage = int(input("Child Age : "))
        self.cgender = input("Child Gender : ")
        print("Father\n", self.fname, " ", self.fage, " ", self.ftalents)
        print("Mother\n", self.mname, " ", self.mage, " ", self.mtalents)
        print("Child\n", self.cname, " ", self.cage, " ", self.cgender)

    def displayTalents(self):
        for i in self.ftalents:
            for j in self.mtalents:
                if i == j:
                    print(i)
                    break


a = Child()
a.getChildDetails()
a.displayTalents()




