#Write a function to return the sum of all numbers in a list.   Sample List : (8, 2, 3, 0, 7)

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

sample_list = (8, 2, 3, 0, 7)

print("Sum:", sum_list(sample_list))