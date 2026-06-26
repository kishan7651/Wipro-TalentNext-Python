#Write a program to create a list of 5 integers and display the list items. Access individual elements through index.

numbers = [10, 20, 30, 40, 50]

print("Complete List:", numbers)

for i in range(len(numbers)):
    print("Element at index", i, "=", numbers[i])
