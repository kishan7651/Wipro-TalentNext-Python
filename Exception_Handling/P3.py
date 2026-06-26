#Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.

# Program to open a file and print its contents in title case

try:
    filename = input("Enter file name: ")

    file = open(filename, "r")
    content = file.read()

    print("File Contents in Title Case:")
    print(content.title())

    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")