#Write a program to accept input from user and append it to a txt file.



file = open("sample.txt", "a")

text = input("Enter text to append: ")

file.write(text + "\n")

file.close()

print("Data appended successfully.")