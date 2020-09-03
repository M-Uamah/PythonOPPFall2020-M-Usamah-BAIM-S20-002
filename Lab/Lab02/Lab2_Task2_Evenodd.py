#Taking number from user and check it is even or odd

enterNumber = int(input("Enter a value: "))
modeValue = enterNumber % 2
if modeValue == 0:
    print(enterNumber,"is an even value")
else:
    print(enterNumber,"is a odd value")


#Taking the range of number from the user to find even and odd using for loop

# taking_a_value = int(input("Enter a value: "))
lowerLimit = int(input("Enter starting value: "))
upperLimit = int(input("Enter end value: "))
for eachNumber in range(lowerLimit,upperLimit+1):
    modeValue = eachNumber % 2
    if modeValue == 0:
        print(eachNumber, "is an even")
    else:
        print(eachNumber, "is an odd")

#Taking the range of number from the user to find even and odd using while loop

# taking_a_value = int(input("Enter a value: "))
lowerLimit = int(input("Enter starting value: "))
upperLimit = int(input("Enter end value: "))

while (lowerLimit <= upperLimit):
    modeValue = lowerLimit % 2
    if modeValue == 0:
        print(lowerLimit, "is an even")
    else:
        print(lowerLimit, "is an odd")
    lowerLimit=lowerLimit+1

#Finding totel number of odd and even in a range using for loop
lowerLimit = int(input("Enter starting value: "))
upperLimit = int(input("Enter end value: "))
evenNumber = 0
oddNumber = 0
for eachNumber in range (lowerLimit, upperLimit+1):
    modeValue = eachNumber % 2
    if modeValue == 0:
        evenNumber = evenNumber + 1
    else:
        oddNumber = oddNumber + 1
print ("Total number of even number is = ",evenNumber)
print ("Total number of odd number is = ",oddNumber)

# Finding totel number of odd and even in a range using while loop
lowerLimit = int(input("Enter starting value: "))
upperLimit = int(input("Enter end value: "))
evenNumber = 0
oddNumber = 0
while (lowerLimit <= upperLimit):
    modeValue = lowerLimit % 2
    if modeValue== 0:
        evenNumber = evenNumber + 1
    else:
        oddNumber = oddNumber + 1

    lowerLimit = lowerLimit + 1
print ("Total number of even number is = ",evenNumber)
print ("Total number of odd number is = ",oddNumber)
