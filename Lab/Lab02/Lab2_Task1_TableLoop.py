#Print table using while loop


num1 = int(input("Enter a number: "))
num2 = int(input("Enter a upper limit: "))
num3 = int(input("Enter a lower limit: "))
i = num2
while (i <= num3):
    print (i,"*",num1,"=",i*num1)
    i=i+1
print("=======================================================")
#Printing table using for loop

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a upper limit: "))
num3 = int(input("Enter a lower limit: "))
for i in range(num2, num3+1):
    print (i,"*",num1,"=",i*num1)
print("=======================================================")
