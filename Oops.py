class calculator :
    num =100

    #default constructor
    def __init__(self, a ,b):
        self.firstnumb=a
        self.secondnumb=b
        print("i am called automatically when object is created")

    def getdata(self):
        print("i am now wxecuting as method in class")

    def sumation(self):
        return self.firstnumb + self.secondnumb + calculator.num


obj= calculator(2,3)
obj.getdata()
print(obj.sumation())

obj1 = calculator(4,5)
obj1.getdata()
print(obj1.sumation())


