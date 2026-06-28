# Reverse String
# Palindrome
# Count Vowels
# Count Characters
# Count Occurrences

name = "vinu"
print(name[::-1])
rev=""

for i in name:
    rev = i + rev
print(rev)

paliname ="madam"

if paliname == paliname[::-1]:
    print("paliname")
else:
    print("not paliname")

rpali=""
for i in paliname:
    rpali = i + rpali
if rpali == paliname[::-1]:
    print("paliname")
else:
    print("not paliname")

vow="automation"
count =0
for i in vow:
    if i in "aeiou":
        count += 1
print(count)

char=0
for i in vow:
    char = len(vow)
print(char)

count1=0
for i in vow:
    count1+=1
print(count1)


