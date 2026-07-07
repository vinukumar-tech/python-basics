#Handle divide-by-zero.
try :
    value = 10/0
except ZeroDivisionError:
    print("ZeroDivisionError")

#Handle invalid integer input.
try :
    value= int("int")
except ValueError:
    print("ValueError")

#Handle file not found.
try :
    with open ("vinu.txt") as file:
        raju=file.read()
        print(raju)
except FileNotFoundError:
    print("FileNotFoundError")

#Handle missing dictionary key.
try:
    employee = {"name": "Raju","age": 25}
    print(employee["salary"])
except KeyError:
    print("Key not found")

#handle list Index error
try:
    imp=["name",32,"float"]
    print(imp[4])
except IndexError:
    print("IndexError")

#Use else.
try:
    imp=["name",32,"float"]
    print(imp[2])
except IndexError:
    print("IndexError")
else :
    print("Name not found")

#use finally
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Finally block executed")

#custom
try:
    age = int(input("Enter age: "))
    if age < 18:
        raise Exception("You are not eligible.")
    print("eligible")
except Exception as e:
    print(e)

#print exception message
try:
    a = 10
    b = 0
    print(a / b)
except Exception as e:
    print("Exception:", e)

#atm withdrawel
try:
    balance = 10000
    amount = int(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")
    if amount > balance:
        raise Exception("Insufficient balance.")
    balance -= amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
except Exception as e:
    print(e)


#Mini Automation Project
try:
    print("Logging in...")
    username = input("Username: ")
    password = input("Password: ")
    if username != "vinu" or password != "123":
        raise Exception("Invalid Credentials")
    print("Login Successful")
except Exception as e:
    print(e)
finally:
    print("Closing Browser")