numbers = [10, 7, 5, 2, 7, 1, 3]
greatest = numbers[0]
for number in numbers:
    if number > greatest:
        greatest = number

print(greatest)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    print(row)

data = [2,4,5,3,5,7,3,5]
data.append(100)
print(data)
data.insert(2, 500)
print(data)
data.remove(5)
print(data)

print(5 in data)
print(data.count(5))

# print(data.index(700))

data.sort()
print(data)


data2 = data.copy()
data2.reverse()
print(data2)

data.clear()
print(data)

items = [2,4,5,3,5,7,3,5,1,34,5,3,5,2,1]
for item in items:
    while items.count(item) > 1:
        items.remove(item)

print(items)