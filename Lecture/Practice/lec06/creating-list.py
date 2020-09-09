#!/usr/bin/env python3
nameList = []
numberList=[]

# for i in range (3):
'''
while True:
    enterName = str(input("Enter name: "))
    enterNumber = int(input("Enter number: "))
    nameList.append(enterName)
    numberList.append(enterNumber)
    print('Do you want to insert another user...')
    want_to_insert = input("Press y to enter a new user or n to eixt: ")
    if want_to_insert == 'y':
        continue
    else:
        break

print(nameList)
print(numberList)
'''
condition = True
while condition == True:
    enterName = str(input("Enter name: "))
    enterNumber = int(input("Enter number: "))
    nameList.append(enterName)
    numberList.append(enterNumber)
    print('Do you want to insert another user...')
    want_to_insert = input("Press y to enter a new user or n to eixt: ")
    if want_to_insert == 'y':
        condition = True
    else:
        condition = False
print(nameList)
print(numberList)
