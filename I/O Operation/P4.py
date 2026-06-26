#Write a program to read contents from a txt file line by line and store each line into a list.

# Read contents from a text file line by line and store in a list

file = open("sample.txt", "r")

lines = []

for line in file:
    lines.append(line.strip())

file.close()

print("Contents of the list:")
print(lines)