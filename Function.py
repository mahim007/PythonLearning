def myFunc(limit):
    for i in range(limit):
        print(i)

print("start")
myFunc(5)
print("end")

def greetUser(firstName, lastName, age, phone):
    print(f"{firstName} {lastName}")
    print(f"{age} {phone}")

firstName = "Ashraful"
lastName = "Mahim"

greetUser(lastName, firstName, age = 25, phone = 123456789)

def sum(n):
    print( round((n * (n + 1)) / 2))


value = sum(5)
if value == None:
    value = "it's None!!"
print(value, sum(5) == None)