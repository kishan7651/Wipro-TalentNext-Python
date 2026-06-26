#Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

sum_prime = 0

# Accept 10 numbers from command line arguments
for i in range(1, 11):
    num = int(sys.argv[i])
    if is_prime(num):
        sum_prime += num

print("Sum of prime numbers =", sum_prime)