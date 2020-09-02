# Creating a calculator using if else condition

print("--------------------------\ncalculator\n--------------------------")
num1 = float(input("Enter a first number: "))
num2 = float(input("Enter a Second number: "))
opp = input("Select an operator +, -, *, / : ")

if opp == "+":
    print(num1 +num2)

elif opp == "-":
    print(num1 - num2)

elif opp == "*":
    print(num1 * num2)

elif opp == "/":
    int(num1)
    int(num2)
    # print (type(num1))
    # print(type(num2))
    print(num1/num2)
    
else:
    print ("Error...\nEnter a correct operator")
