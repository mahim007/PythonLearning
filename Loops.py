i = 1
while i <= 10:
    print('*' * i)
    i += 1
print("done!")

num = 7
counter = 1
while counter <= 5:
    guess = int(input("guess a number: "))
    if guess == num:
        print("you win!")
        break
    counter += 1
else:
    print("you loose!")