emails= ["a@test.com","b@test.com","a@test.com"]

print(set(emails))

ui_users= {"Vinu","Rahul","John"}
db_users= {"Rahul","John","David"}
print(ui_users.intersection(db_users))

#remove duplicates
env=["bdc","uat","uat","bdc","prod","sit"]
fruit=["orange","grapes","mango","bdc"]
print(set(env).intersection(set(fruit)))

#differnece
print(set(env).difference(set(fruit)))

#add an element
env1={"bdc","uat","uat","bdc","prod","sit"}
env1.add("apple")
print(env1)

#remove
env1.remove("prod")
print(env1)

#check membership
if "uat" in env1:
    print("uat is present")

#count unique values
print(len(env1))

#merge 2 sets
a={1,2,3}
b={4,5,6}
v=a.union(b)
print(v)

for i in v:
    print(i)

#convert list to set
print(set(fruit))

#mini automation project
ui_products= {"Laptop","Mouse","Keyboard","Monitor"}
db_products= {"Laptop","Keyboard","Webcam","Monitor"}

# Common products
common = ui_products.intersection(db_products)
print("Common Products:", common)

# Missing in DB (present in UI only)
missing_in_db = ui_products.difference(db_products)
print("Missing in DB:", missing_in_db)

miss_inUI=db_products.difference(ui_products)
print("Missing in UI:", miss_inUI)

print(len(sorted(ui_products.union(db_products))))
