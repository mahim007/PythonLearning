condition1 = False
condition2 = False

if condition1 and condition2:
    print("true")
elif condition1 or condition2:
    print("at least true")
else:
    print("false")


print(not condition1)

temperature = 30
if temperature == 32:
    print("not a hot day")
else:
    print("a hot day")


name = input("write your name: ")
if len(name) > 10:
    print("It's a long name.")
else:
    print("it's a short name.")