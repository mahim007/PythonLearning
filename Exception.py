try:
    age = int(input("enter age: "))
    print("your age: ", age)
    avg = 1000 / age
    print("avg: ", avg)
except ValueError:
    print("non numerical input detected!")
except ZeroDivisionError:
    print("division by zero detected!")