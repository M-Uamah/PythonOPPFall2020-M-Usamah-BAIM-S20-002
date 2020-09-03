#Taking number from user and check it is even or odd

taking_a_value = int(input("Enter a value: "))
modevalue = taking_a_value % 2
if modevalue == 0:
    print(taking_a_value,"is an even value")
else:
    print(taking_a_value,"is a odd value")


#Taking the range of number from the user to find even and odd using for loop

# taking_a_value = int(input("Enter a value: "))
upperlimit = int(input("Enter Upperlimit: "))
lowerlimit = int(input("Enter Lowerlimit: "))
for eachnumber in range(upperlimit,lowerlimit+1):
    modevalue = eachnumber % 2
    if modevalue == 0:
        print(eachnumber, "is an even")
    else:
        print(eachnumber, "is an odd")

#Taking the range of number from the user to find even and odd using while loop

# taking_a_value = int(input("Enter a value: "))
upperlimit = int(input("Enter Upperlimit: "))
lowerlimit = int(input("Enter Lowerlimit: "))
i = upperlimit
while (i <= lowerlimit):
    modevalue = eachnumber % 2
    if modevalue == 0:
        print(i, "is an even")
    else:
        print(i, "is an odd")
    i=i+1
