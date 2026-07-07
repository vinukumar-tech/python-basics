#Student class
class Student:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Student Name:", self.name)
stud = Student("Vinu")
stud.display()

#multiple objects
class Fruit:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Fruit Name:", self.name)
fruit1 = Fruit("Mango")
fruit2 = Fruit("Apple")
fruit1.display()
fruit2.display()

#print employee details
class employee_details:
    def __init__(self, name , salary , age ):
        self.name = name
        self.salary = salary
        self.age = age
    def display(self):
        print("emplyee name ", self.name)
        print("emplyee salary ", self.salary)
        print("emplyee age ", self.age)

emp=employee_details("vinu",500000,30)
emp.display()

# Inheritance

class Vehicles:
    def __init__(self, name, capacity, years):
        self.name = name
        self.capacity = capacity
        self.years = years
    def display(self):
        print("Vehicle Name:", self.name)
        print("Vehicle Capacity:", self.capacity)
        print("Vehicle Years:", self.years)
class Vehicle_Details(Vehicles):
    def car(self):
        print("Vehicle Details")
pn = Vehicle_Details("Venue", 5, 10)
pn.display()
pn.car()

#polymorphism
class Dog :
    def sound(self):
        print("dog sound")
class cat:
    def sound(self):
        print("cat sound")

dog = Dog()
cat = cat()
dog.sound()
cat.sound()

#encapsulation
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display (self):
        print("Employee Name:", self.name)

emp=employee("Vinu",500000)
emp.display()


#create a car class
class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def display(self):
        print("Car Name:", self.name)
        print("Car Model:", self.model)

car = Car("Venue", 5000)
car.display()

#create a bank account class
# Create a Bank Account class

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Bank Account Name:", self.name)
        print("Balance after deposit:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Bank Account Name:", self.name)
        print("Balance after withdrawal:", self.balance)

account = BankAccount("Vinu", 10000)

account.deposit(100)
account.withdraw(10)

#browser class
class Browser:
    def launch(self):
        print("Browser Launched")

    def close(self):
        print("Browser Closed")

browser = Browser()

browser.launch()
browser.close()

#Mini Automation Project

class   BasePage:
    def open_browser(self):
        print("Browser Opened")
    def close_browser(self):
        print("Browser Closed")

class   LoginPage(BasePage):
    def login(self):
        print("Login Successful")

page = LoginPage()
page.open_browser()
page.login()
page.close_browser()