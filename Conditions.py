#conditions
greeting = "Hello"

if greeting == "morning":
    print("condition matches")
    print("second condition matches")
else:
    print("condition does not match")
print("if condition code completed")

a=3
if greeting == a>2:
    print("condition matches")
    print("second condition matches")
else:
    print("condition does not match")
print("if condition ")


#for loop
obj = [2,3,4,5,6]

for i in range (len(obj)):
    print(obj[i])
print("end")

for i in obj:
    print(i)

for i in obj:
    print(i*2)

#sum of first natural number 1=2=3=4=5= 50

for j in range(1,6): #range(i,j) -> i to j-1
    print(j)

sum = 0
for j in range(1,6): #range(i,j) -> i to j-1
    sum = sum + j
print(sum)

#for 2 index diff
for k in range(1,10 , 2):
    print(k)

for km in range(10):
    print(km)
