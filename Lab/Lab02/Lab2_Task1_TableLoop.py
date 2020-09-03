#Print table using while loop


tablenumber = int(input("Enter a number: "))
upperlimit = int(input("Enter a upper limit: "))
lowerlimit = int(input("Enter a lower limit: "))
i = upperlimit
while (i <= lowerlimit):
    print (i,"*",tablenumber,"=",i*tablenumber)
    i=i+1
print("=======================================================")
#Printing table using for loop

tablenumber = int(input("Enter a number: "))
upperlimit = int(input("Enter a upper limit: "))
lowerlimit = int(input("Enter a lower limit: "))
for foreachnumber in range(upperlimit, lowerlimit+1):
    print (i,"*",tablenumber,"=",i*tablenumber)
print("=======================================================")
