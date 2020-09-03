#Print table using while loop

i = 1
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
while (i <= num2):
    print (i,"*",num1,"=",i*num1)
    i=i+1
print("=======================================================")
#Printing table using for loop

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

for i in range(0, num2+1):
    print (i,"*",num1,"=",i*num1)
print("=======================================================")
