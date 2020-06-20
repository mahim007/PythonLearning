for item in ["Python", "Java", "Javascript"]:
    print(item)


for data in range(1, 10, 3):
    print(data)


prices = [1,2,3,4,5]
total = 0
for i in range(len(prices)):
    total += prices[i]

print(f"total: {total}" )

prices = [1,2,3,4,5]
total = 0
for price in prices:
    total += price

print(f"total: {total}" )

xCoord = int(input("enter x coordinate: "))
yCoord = int(input("enter y coordinate: "))

for x in range(xCoord):
    for y in range(yCoord):
        print(f"{x} {y}")


xCoord = int(input("enter x coordinate: "))
yCoord = int(input("enter y coordinate: "))

for x in range(1, xCoord+1):
    print("*" * yCoord)

print("")
print("")

numbers = [5, 2, 5, 2, 2]
for x in numbers:
    line = ""
    for y in range(x):
        line += "X"
    print(line)