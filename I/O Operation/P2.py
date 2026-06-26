#Write a program to read first n lines from a txt file. Get n as user input.

# Read first n lines from a text file

file = open("sample.txt", "r")

n = int(input("Enter the number of lines to read: "))

for i in range(n):
    line = file.readline()
    if line == "":
        break
    print(line, end="")

file.close()