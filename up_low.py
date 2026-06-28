#Reverse a string without using [::-1]

text = "Vinu123QA"
upper_count = 0
lower_count = 0
digit_count = 0

for i in text:
    if i.isupper():
        upper_count +=1
    elif  i.islower():
        lower_count +=1
    elif i.isdigit():
        digit_count += 1

print("Uppercase:",upper_count)
print("Lowercase:",lower_count)
print("Digits:",digit_count)
