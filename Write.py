# file = open("test.txt", "w")
# file.close()
from certifi import contents

#method 2
with open("text.txt", "r") as reader:
   content = reader.readlines()
   reversed(content)
   with open("text.txt", 'w') as writer:
        for line in content:
           writer.write(line)