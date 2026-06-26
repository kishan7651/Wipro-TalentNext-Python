#Write a function to print the even numbers from a given list. List is passed to the function as an argument.   Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] Expected Result : [2, 4, 6, 8]

def even_numbers(lst):
    even_list = []

    for num in lst:
        if num % 2 == 0:
            even_list.append(num)

    print(even_list)

# Sample List
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers(sample_list)