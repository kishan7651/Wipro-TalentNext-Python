#Write a function to calculate and return the factorial of a number (a non-negative integer)

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."

    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact

num = int(input("Enter a non-negative integer: "))
print("Factorial:", factorial(num))