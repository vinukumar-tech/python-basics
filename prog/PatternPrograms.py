for i in range (5, 0 , -1):
    print(i * "*")
# *****
# ****
# ***
# **
# *


for i in range (1,6):
    print("*" * i)
# *
# **
# ***
# ****
# *****

for i in range (6):
    print ("*" * 6)
# ******
# ******
# ******
# ******
# ******
# ******

for i in range (5):
    print("*")
# *
# *
# *
# *
# *

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

rows = 5
for i in range(rows):
    print(" " * (rows - i - 1) + "* " * (i + 1))

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

