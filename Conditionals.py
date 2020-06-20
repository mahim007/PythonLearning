condition = False
anotherCondition = False
if condition:
    print("do it")
    print("do it right now")
elif anotherCondition:
    print("did you do it yesterday?")
    print("are you sure?")
else:
    print("do it tomorrow")
    print("you have another day")
print("best of luck!")

price = 1000000
goodCredit = False
if goodCredit:
    price = price - (price * 0.10)
else:
    price = price - (price * 0.20)
print(price)