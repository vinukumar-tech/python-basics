#print numbers
for i in range (1,10):
    print(i)
for i in range (10,1,-1):
    print(i)
for i in range (1 , 100 , 2):
    print(i)
for i in range (1,100):
    if i % 2 != 0:
        print(i)
sum=0
for i in range (1,100):
    sum = sum + i
    print(sum)
count=0
name="vinu"
for ch in name :
    if ch in ("AEIOU"):
        count = count + 1
        print(ch)
rev=""
for ch in name :
    rev = ch + rev
print(rev)




users=["admin","HR","manager","Employee"]
for user in users :
    if user == "admin":
        print(f"Logging in as {user}")
    elif user == "HR":
        print(f"Logging in as {user}")
    elif user == "manager":
        print(f"Logging in as {user}")
        if user == "manager":
            print(f"{user} account is locked, skipping login")
    else :
        print(f"Logging in as {user}")


print("###################################################")

for user in users :
    print(f"Logging in as {user}")
