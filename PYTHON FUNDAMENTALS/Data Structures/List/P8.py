#Write a program to remove the first occurrence of a specified element from a list.
numbers = [10, 20, 30, 20, 40]

element = int(input("Enter element to remove: "))

numbers.remove(element)

print(numbers)
