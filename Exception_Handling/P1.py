#Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.

# Program to perform division using exception handling

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except Exception as e:
    print("Error:", e)

else:
    print("Result =", result)