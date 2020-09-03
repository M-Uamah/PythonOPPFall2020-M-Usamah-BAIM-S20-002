#Print table using while loop
i = 1
num1 = int(input("Enter a number: "))
while (i <= 10):
    print (i,"*",num1,"=",i*num1)
    i=i+1
print("=======================================================")
#Printing table using for loop

num1 = int(input("Enter a number: "))

for i in range(0, 11):
    print (i,"*",num1,"=",i*num1)
print("=======================================================")