#Write a program to read the entire content from a txt file and display it to the user.



file = open("sample.txt", "r")

content = file.read()

print("File Contents:")
print(content)

file.close()