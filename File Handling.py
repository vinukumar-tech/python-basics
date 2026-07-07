file= open("text.txt", "r")
content = file.read()
print(content)
file.close()

#withopen , Read a text file.
with open ("text.txt", "r") as file:
    content = file.read()
    print(content)
#Write data to a file.
with open("text.txt", "w") as file:
    file.write("Amazon\n")
    print("data written")

#Append data.
with open("text.txt","a")as file:
    file.write("flipkart\n")
    print("data appended")

#Count lines in a file.
count=0
with open("text.txt","r") as file:
    for i in file:
       count+=1
print(count)

#Count lines in a file.
with open("text.txt","r") as file:
    lines = file.readlines()
print("total lines",len(lines))

#Count words in a file.
with open("text.txt","r") as file:
    content = file.read()
    words = content.split()
print("total words",len(words))

#Count characters.
with open("text.txt","r")as file:
   content=file.read()
print(len(content))

#Search for a word.
word = input("Enter the word to search: ")
with open("text.txt", "r") as file:
    content = file.read()
if word in content:
    print("Word found")
else:
    print("Word not found")

#Copy one file to another.
with open("text.txt", "r") as source:
    content = source.read()
with open("copy.txt", "w") as destination:
    destination.write(content)
print("File copied successfully.")

#Read line by line.with open("text.txt", "r") as file:
with open("text.txt", "r") as file:
    for line in file:
        print(line, end="")

#Print only lines containing "ERROR".
with open("text.txt", "r") as file:
    for line in file:
        if "ERROR" in line:
            print(line, end="")


#Mini Automation Project
with open("users.txt","r")as file:
    for user in file:
        print("Logging in as ", user.strip())