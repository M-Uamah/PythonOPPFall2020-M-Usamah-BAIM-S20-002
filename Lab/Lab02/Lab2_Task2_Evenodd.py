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
for eachnumber in range(lowerLimit,upperLimit+1):
    modeValue = eachnumber % 2
    if modeValue == 0:
        print(eachnumber, "is an even")
    else:
        print(eachnumber, "is an odd")

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
evennumber = 0
oddnumber = 0
for eachnumber in range (lowerLimit, upperLimit+1):
    modeValue = eachnumber % 2
    if modeValue == 0:
        evennumber = evennumber + 1
    else:
        oddnumber = oddnumber + 1
print ("Total number of even number is = ",evennumber)
print ("Total number of odd number is = ",oddnumber)

# Finding totel number of odd and even in a range using while loop
lowerLimit = int(input("Enter starting value: "))
upperLimit = int(input("Enter end value: "))
evennumber = 0
oddnumber = 0
while (lowerLimit <= upperLimit):
    modeValue = lowerLimit % 2
    if modeValue== 0:
        evennumber = evennumber + 1
    else:
        oddnumber = oddnumber + 1

    lowerLimit = lowerLimit + 1
print ("Total number of even number is = ",evennumber)
print ("Total number of odd number is = ",oddnumber)
