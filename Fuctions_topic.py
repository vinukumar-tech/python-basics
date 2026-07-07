#mini automation program
import random


def launch_browser():
    print("Launching Browser")
def login(username,password):
    print(f"Login Successful{username}")
def search_employee(empid):
    print(f"search_employee{empid}")
def logout():
    print("Logout Successful")

launch_browser()
login("vinu","password")
search_employee("emp123")
logout()

#print ur name
def names(name):
    print(f"Name : {name}")
names("vinu")

def add(a,b):
    return a+b
print(add(1,2))

def sub(a,b):
    return a -b
result = add(2,4)
print(result)

def sq (a, b):
    return a*a+b
result = sq(2,4)
print(result)

def square (num):
    return num*num
result = square(3)
print(result)
print("**************************************************")
def even_odd(numb):
    if numb % 2==0:
        return numb
    else:
        return numb+1

print(even_odd(5))

def rev(string):
    strings=string[::-1]
    return strings
print(rev(input("Enter a string: ")))


def counts(word):
    count=0
    for ch in word:
        if ch.lower() in "aeiou":
            count += 1
    return count
print(counts(input("Enter a string: ")))

def large(a ,b, c):
    largest=0
    if a>=b and a>=c:
        largest=a
    elif b>=a and b>=c:
        largest=b
    else:
        largest=c
    return largest
print(large(10,15,20))

#factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(factorial(5))

# function to generate randon emp id

def random_emp():
    return random.randint(1,100)
print(random_emp())

#real project scenerio


