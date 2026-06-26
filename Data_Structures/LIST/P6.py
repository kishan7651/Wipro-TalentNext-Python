#Write a program to insert a new item before the second element in an existing list.

numbers = [10, 20, 30, 40]

new_item = int(input("Enter new item: "))

numbers.insert(1, new_item)

print(numbers)

