Name= "Digital 123"
print(f"first ch {Name[0]}")
print(Name[-1])
print(Name[::-1])

count=0
for ch in Name:
    if ch.lower() in "aeiou":
        count+=1
print("count vowels+", count)

for ch in Name:
    if ch.lower() not in "aeiou":
        count+=1
print("count vowels+", count)

#length
print(len(Name))

#count digits
digits=0
for ch in Name:
    if ch.isdigit():
        digits+=1
print("count digits+", digits)

#count space
space=0
for ch in Name:
    if ch == " ":
        space+=1
print("count space+", space)

#palindrome
if Name == Name[::-1]:
    print("palindrome")
else:
    print ("not palindrome")

#remove first and last space
print(Name.strip())
#using replace
strip=Name.replace(" ","")
print(strip)

#using loop
result=""
for ch in Name:
    if ch != " ":
        result += ch
print(result)

#replace one word with another
replace=Name.replace("123", "Product")
print(replace)

#split a sentence into words
print(Name.split())

#join words using "-"
print("-".join(Name))

#convert to uppercase / lower
print(Name.upper())
print(Name.lower())

#capitalize each word
print(Name.capitalize())

# to check if the Name starts with Https
if Name.startswith("https"):
    print("https")
else:
    print("http")

#to check file name ends with .com
if Name.endswith(".com"):
    print("com")
else:
    print("not com")

#count occurrence of the character
count1=0
for ch in Name:
    if ch == "a":
        count1+=1
print(count1)
print(Name.count("a"))

checked=""
count2=0

for ch in Name:
    if ch not in checked:
        count2+=0
        for ch2 in Name:
            if ch == ch2:
                count2+=1
        print(ch,":" ,count2)
        checked+=ch
#find index of char
print(Name[4])
print(Name.find("t"))

#Suppose a website displays:`
# Welcome Vinu Kumar

# 1. Check if `"Welcome"` exists.
# 2. Convert the message to uppercase.
# 3. Count the total characters.
# 4. Extract only the username (`Vinu Kumar`).
# 5. Replace `"Welcome"` with `"Hello"`.

website = "welcome vinu kumar"
count = 0
if "welcome" in website:
    print("welcome")
print(website.upper())
print(len(website))
name=" ".join(website.split()[1:])
print(name)
replace = website.replace("welcome","Hello")
print(replace)