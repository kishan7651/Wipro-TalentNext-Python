#Given two non-negative values, print true if they have the same last digit, such as with 27 and 57. lastDigit(7, 17) → true lastDigit(6, 17) → false lastDigit(3, 113) → true if else4M 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 10 == num2 % 10:
    print(True)
else:
    print(False)
