# Taking number from user and check it is Prime Number or not

enterNumber = int(input("Enter a number: "))
if enterNumber > 1:
    primeNumber = enterNumber % 2
    if primeNumber == 0:
        print(enterNumber, "is not a primer number")
    else:
        print(enterNumber, "is a primer number")
else:
    print(enterNumber, "is not a primer number")
