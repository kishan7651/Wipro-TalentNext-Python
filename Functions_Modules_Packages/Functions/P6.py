#Write a function that takes a number as a parameter and checks whether the number is prime or not.

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")