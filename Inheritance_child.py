from Oops import calculator

class child(calculator):
    num2=200

    def __init__(self):
        calculator.__init__(self,2,10)


    def getcompletedata(self):
        return self.firstnumb + self.secondnumb + calculator.num +child.num2 + self.sumation()


obj = child()
print(obj.getcompletedata())