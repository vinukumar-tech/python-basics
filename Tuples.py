abc=(1,2,3,4,5)
print(abc[0])
print(abc[-1])
print(len(abc))
print(abc.count(3))
count=0
for x in abc:
    if x==2:
        count+=1
        print(count)

#index of value
print(abc.index(4))

for x in abc:
    print(x)

if 5 in abc:
    print("present")

a="pen","ten", "sin"
print(a[2])

writing,digits,red=a
print(writing)

#mini Automation Project
ENVIRONMENTS= ("DEV","QA","UAT","PROD")
print(ENVIRONMENTS)
if "QA" in ENVIRONMENTS:
    print("QA is supported")
else:
    print("QA is not supported")
print(len(ENVIRONMENTS))
print(ENVIRONMENTS[0])
print(ENVIRONMENTS[-1])