#array list
values = [1,2,3,4,5,6,7,8, "vinu" ,2.4]
print(values)
print(values[0])
print(values[1])
print(values[2])

print(values[-1]) #2.4
print(values[1:5]) #[2, 3, 4, 5]
print(values[:5]) # [1, 2, 3, 4, 5]
values.insert(9,"kumar")
print(values)  #[1, 2, 3, 4, 5, 6, 7, 8, 'vinu', 'kumar', 2.4]

values.append("R")
print(values) #[1, 2, 3, 4, 5, 6, 7, 8, 'vinu', 'kumar', 2.4, 'R']

values[2]="varsha"
print(values) #[1, 2, 'varsha', 4, 5, 6, 7, 8, 'vinu', 'kumar', 2.4, 'R']

del values[0]
print(values) #[2, 'varsha', 4, 5, 6, 7, 8, 'vinu', 'kumar', 2.4, 'R']

del values[1]
print(values)
del values[2]
print(values)
del values[-1]
print(values)

#tupple - same as list data type but immutable
val=(1,2,"vinu",4,)
print(val)

#dictionary
dic={"name":"vinu" ,"age":25,1:"one",2:2}
print(dic)
print(dic["name"])
print(dic["age"])
print(dic[1])
print(dic[2])

#create a dictionary
dict={}
dict["name"]="vinu"
dict["age"]=25
dict["Lastname"]="kumar"
print(dict)  #{'name': 'vinu', 'age': 25, 'Lastname': 'kumar'}
print(dict["name"])  #vinu

