phone=["samsung","nokia", "apple" , "realme"]
phone.append("Mi")
print(phone)
phone.remove("nokia")
print(phone)

#largest
largest=0
lar=[2,4,6,8,9,]
for i in lar:
    if i > largest:
        largest=i
print(largest)

#smallest
smallest=lar[0]
lar=[2,4,6,8,9,]
for i in lar:
    if i < smallest:
        smallest=i
print(smallest)

#second largest numb
lar.sort()
print(lar[-2])

#without sort
largest=0
second =0
for i in lar:
    if i > largest:
        second = largest
        largest=i
    elif i > second:
        second = i
print(second)

#remove duplicates
dup=[1,2,1,2,1,2,3,4,5,6]
print(list(set(dup)))

#without using set
unique=[]
for i in dup:
    if i not in unique:
        unique.append(i)
print(unique)

#reverse a list
print(list(dup[::-1]))

dup.reverse()
print(dup)

reversed_list= list(reversed(dup))
print(reversed_list)

#sort ascending
dup.sort()
print(dup)

#sort decending
dup.sort(reverse=True)
print(dup)

#count even or odd
even = 0
odd =0

for i in dup:
    if i % 2==0:
        even+=1
    else:
        odd+=1
print("even",even)
print("odd",odd)

#merge 2 lists
a=[1,2,3,4]
b=[5,6,7]
print(a+b)

a.extend(b)
print(a)

#check the element exit
a=[1,2,3,4]
if 2 in a:
    print("element is present")

#copy a list
list1=[1,2,2,3]
list2=list(list1)
print(list2)

#find the sum of all numbers
list3=[2,3,4]
print(sum(list3))

#find the average
l1=[1,2,3,4,5]
average=sum(l1)/len(l1)
print(average)



#mini automation project
products= ["Laptop","Mouse","Keyboard","Monitor"]
print(products)
print(len(products))
if "Mouse" in products:
    print("Mouse is present")

products.sort()
print(products)

products.append("webcam")
print(products)
products.remove("Keyboard")
print(products)

#assignment
employees= ["Vinu","Rahul","John","David","Amit"]
print(employees[0])
print(employees[-1])
employees.append("Kiran")
employees.remove("John")
employees.sort()
print(employees)
print(len(employees))
if "Rahul" in employees:
    print("Rahul is present")
for employee in employees:
    print(employee)