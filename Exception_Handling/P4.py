#Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.


# Program to check whether the number at a given index is positive or negative

numbers = [10, -5, 25, -8, 15, -20, 30, -12, 40, -1]

try:
    index = int(input("Enter the index (0-9): "))

    if numbers[index] >= 0:
        print("The number is Positive.")
    else:
        print("The number is Negative.")

except IndexError:
    print("Error: Invalid index entered.")