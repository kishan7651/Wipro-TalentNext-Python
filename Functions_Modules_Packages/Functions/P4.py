#Write a function that accepts a string and prints the number of upper case letters and lower case letters in it. 

def count_case(string):
    upper = 0
    lower = 0

    for ch in string:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("Number of uppercase letters:", upper)
    print("Number of lowercase letters:", lower)

# Example
sample_string = "The Quick Brown Fox"

count_case(sample_string)