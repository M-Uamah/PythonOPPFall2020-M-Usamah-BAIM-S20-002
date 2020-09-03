#Taking number from user and check it is even or odd

enternumber = int(input("Enter a value: "))
modevalue = enternumber % 2
if modevalue == 0:
    print(enternumber,"is an even value")
else:
    print(enternumber,"is a odd value")


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

while (upperlimit <= lowerlimit):
    modevalue = upperlimit % 2
    if modevalue == 0:
        print(upperlimit, "is an even")
    else:
        print(upperlimit, "is an odd")
    upperlimit=upperlimit+1

#Finding totel number of odd and even in a range using for loop
upperlimit = int(input("Enter Upperlimit: "))
lowerlimit = int(input("Enter Lowerlimit: "))
evennumber = 0
oddnumber = 0
for eachnumber in range (upperlimit, lowerlimit+1):
    modevalue = eachnumber % 2
    if modevalue == 0:
        evennumber = evennumber + 1
    else:
        oddnumber = oddnumber + 1
print ("Total number of even number is = ",evennumber)
print ("Total number of even number is = ",oddnumber)

# Finding totel number of odd and even in a range using while loop
upperlimit = int(input("Enter Upperlimit: "))
lowerlimit = int(input("Enter Lowerlimit: "))
evennumber = 0
oddnumber = 0
while (upperlimit <= lowerlimit):
    # modevalue = upperlimit % 2
    if upperlimit%2 == 0:
        evennumber = evennumber + 1
    else:
        oddnumber = oddnumber + 1
print ("Total number of even number is = ",evennumber)
print ("Total number of even number is = ",oddnumber)
