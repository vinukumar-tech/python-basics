number = 200
num2 = 100
num3 = 50
if number == 200:
    print("positive")
else:
    print("negative")

if number % 2 ==0:
    print("even")
else:
    print("odd")

if number > num2:
    print("number is greater than number2")
else:
    print("number is not greater than number2")

if number >num2 and number > num3:
    print("number is greater than number2")
elif num2 > number and num2 > num3:
    print("number is greater than number3")
else:
    print("number is not greater than number3")

age = 20
if age >= 18:
    print("Age is greater than 18")
else:
    print("Age is less than 18")

Username = input("Enter your username: ")
password = input("Enter your password: ")

if Username == "Admin" and password == "admin123":
    print ("Login Successfull")
    userrole=input("Enter your role: ")
    if userrole == "Admin":
            print("Admin logged")
    elif userrole == "manager":
            print("Manager logged")
    elif userrole == "Employee":
            print("employee logged")
    else:
            print("Login Failed")
else:
    print ("Invalid username or password")



