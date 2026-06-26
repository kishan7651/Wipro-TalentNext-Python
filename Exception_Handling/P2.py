#Write a program to accept a number from the user and check whether it’s prime or not. If user enters anything other than number, handle the exception and print an error message.

# Program to check whether a number is prime using exception handling

try:
    num = int(input("Enter a number: "))

    if num <= 1:
        print(num, "is Not a Prime Number")
    else:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print(num, "is a Prime Number")
        else:
            print(num, "is Not a Prime Number")

except ValueError:
    print("Error: Please enter a valid number.")