numbers = [10, 20, 30, 40, 50]

largest = 0
second = 0

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second:
        second = num

print(second)