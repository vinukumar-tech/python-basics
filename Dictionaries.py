from Lists import employee

Employee={"name":"raju","age":25,"salary":500}
print(list(Employee.keys()))
print(list(Employee.values()))
Employee["city"]="bangalore"
print(list(Employee))

Employee["salary"]=1000
print(list(Employee))

del Employee["city"]
print(list(Employee))

for key in Employee:
    print(key)

dic={"a":{"one":1,"two":2,"three":3},
"a2":{"four":4,"two":2,"three":3}}

print(dic)

print(len(dic.keys()))
if "age" in employee:
    print(employee["age"])

#mini automation project
config= {"browser":"Chrome",
"url":"https://opensource-demo.orangehrmlive.com",
"username":"Admin",
"password":"admin123",
"timeout":20}


print(config["browser"])
print(config["url"])
print(config["username"])
print(config["password"])

config["timeout"]=30
print(config["timeout"])

config["environment"]="QA"
print(config)

for key,value in config.items():
    print(key,value)