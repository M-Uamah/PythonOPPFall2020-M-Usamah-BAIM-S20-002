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
    num3 = int(num1)
    num4 = int(num2)
    # print(type(num3))
    # print(type(num4))
    print(num3/num4)
    
else:
    print ("Error...\nEnter a correct operator")
